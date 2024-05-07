import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
import json
from .models import *
from .serializers import *
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification




class CreateEmployeeMessage(AsyncWebsocketConsumer):
	async def connect(self):
		self.chat_id = self.scope['url_route']['kwargs']['chat_id']
		self.user_id = self.scope['url_route']['kwargs']['user_id']
		self.room_group_name = str(self.chat_id)
		messages = await self.get_chat_msgs(self.chat_id)


		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)

		chat_owner = await self.get_chat_owner(self.chat_id)

		if chat_owner == int(self.user_id) or await self.is_manager(self.user_id):
			await self.accept()
		else:
			raise ValueError('this is not your chat')

	


		for message in messages:
			await self.send(text_data=json.dumps(message))


	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']


		user = await self.get_user(self.user_id)
		chat = await self.get_chat(self.chat_id)

		try:
			await self.get_manager(user.id)
			msg = ChatMessage(sender=user,content=message, chat=chat, sent_user=False)
		except Management.DoesNotExist:
			msg = ChatMessage(sender=user,content=message, chat=chat, sent_user=True)

			

		serializer = MessageSerializer(msg,many=False)
		await self.save_message(msg)


		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type':'chat_message',
				'id' : serializer.data['id'],
				'sender' : serializer.data['sender'],
				'content': serializer.data['content'],
				'timestamp': serializer.data['timestamp'],
				'sent_user': serializer.data['sent_user'],				
				'chat': serializer.data['chat']				
			}
		)

	async def chat_message(self, event):
		id = event['id']
		content = event['content']
		sender = event['sender']
		timestamp = event['timestamp']
		sent_user = event['sent_user']
		chat = event['chat']
		await self.send(text_data=json.dumps({
			'id':id,
			'sender': sender,
			'content': content,
			'timestamp': timestamp,
			'sent_user': sent_user,
			'chat': chat
		}))

	@database_sync_to_async
	def send_to_client(self,chat,title,body):
		device = FCMDevice.objects.filter(user=chat.user)
		device.send_message(
			message=Message(
				notification=Notification(
					title=title,
					body=body
				),
			),
		)



	@database_sync_to_async
	def send_to_all(self,title,body):
		employees = Employee.objects.values_list('phonenumber',flat=True)
		users = CustomUser.objects.filter(phonenumber__in=employees).values_list('id',flat=True)
		devices = FCMDevice.objects.filter(user__in=users)
		for device in devices:
			device.send_message(
				message=Message(
					notification=Notification(
						title=title,
						body=body,
					),
				),
			)


	@database_sync_to_async
	def get_user_ids(self):
		return Management.objects.values_list('id',flat=True)


	@database_sync_to_async
	def get_device(chat):
		return FCMDevice.objects.filter(user=chat.user)


	@database_sync_to_async
	def get_devices(self,user_ids):
		return FCMDevice.objects.filter(user__in=user_ids).values_list('registration_id', flat=True)



	@database_sync_to_async
	def get_chat_msgs(self,chat_id):
		messages = ChatMessage.objects.filter(chat=chat_id)
		serializer = MessageSerializer(messages,many=True)
		return serializer.data



	@database_sync_to_async
	def get_manager(self,user):
		user = CustomUser.objects.get(id=user)
		return Management.objects.get(user=user) or None


	@database_sync_to_async
	def get_user(self, user_id):
		return CustomUser.objects.get(id=user_id)

	@database_sync_to_async
	def get_chat(self, chat_id):
		return Chat.objects.get(id=chat_id)

	@database_sync_to_async
	def get_chat_owner(self, chat_id):
		chat = Chat.objects.get(id=chat_id)
		return int(chat.user.id)


	@database_sync_to_async
	def is_manager(self, user_id):
		user = CustomUser.objects.get(id=user_id)
		if Management.objects.filter(user=user).exists():
			return True
		else:
			return False	
		
	@database_sync_to_async
	def save_message(self, msg):
		msg.save()

	async def disconnect(self, close_code):
		pass












class CreateGuideMessage(AsyncWebsocketConsumer):
	async def connect(self):
		self.chat_id = self.scope['url_route']['kwargs']['chat_id']
		self.user_id = self.scope['url_route']['kwargs']['user_id']
		self.room_group_name = str(self.chat_id)
		messages = await self.get_chat_msgs(self.chat_id)


		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)

		chat_owner = await self.get_chat_owner(self.chat_id)

		if chat_owner == int(self.user_id) or await self.is_guide(self.user_id):
			await self.accept()
		else:
			raise ValueError('this is not your chat')

	

		for message in messages:
			await self.send(text_data=json.dumps(message))


	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		user = await self.get_user(self.user_id)
		chat = await self.get_chat(self.chat_id)

		try:
			await self.get_guide(user.id)
			msg = ChatMessage(sender=user,content=message, chat=chat, sent_user=False)
		except Guide.DoesNotExist:
			msg = ChatMessage(sender=user,content=message, chat=chat, sent_user=True)

		serializer = MessageSerializer(msg,many=False)
		await self.save_message(msg)


		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type':'chat_message',
				'id' : serializer.data['id'],
				'sender' : serializer.data['sender'],
				'content': serializer.data['content'],
				'timestamp': serializer.data['timestamp'],
				'sent_user': serializer.data['sent_user'],				
				'chat': serializer.data['chat']				
			}
		)

	async def chat_message(self, event):
		id = event['id']
		content = event['content']
		sender = event['sender']
		timestamp = event['timestamp']
		sent_user = event['sent_user']
		chat = event['chat']
		await self.send(text_data=json.dumps({
			'id':id,
			'sender': sender,
			'content': content,
			'timestamp': timestamp,
			'sent_user': sent_user,
			'chat': chat
		}))

	@database_sync_to_async
	def send_to_client(self,chat,title,body):
		device = FCMDevice.objects.filter(user=chat.user)
		device.send_message(
			message=Message(
				notification=Notification(
					title=title,
					body=body
				),
			),
		)



	@database_sync_to_async
	def send_to_all(self,title,body):
		managers = Guide.objects.values_list('phonenumber',flat=True)
		users = CustomUser.objects.filter(phonenumber__in=managers).values_list('id',flat=True)
		devices = FCMDevice.objects.filter(user__in=users)
		for device in devices:
			device.send_message(
				message=Message(
					notification=Notification(
						title=title,
						body=body,
					),
				),
			)


	@database_sync_to_async
	def get_user_ids(self):
		return Guide.objects.values_list('id',flat=True)


	@database_sync_to_async
	def get_device(chat):
		return FCMDevice.objects.filter(user=chat.user)


	@database_sync_to_async
	def get_devices(self,user_ids):
		return FCMDevice.objects.filter(user__in=user_ids).values_list('registration_id', flat=True)



	@database_sync_to_async
	def get_chat_msgs(self,chat_id):
		messages = ChatMessage.objects.filter(chat=chat_id)
		serializer = MessageSerializer(messages,many=True)
		return serializer.data



	@database_sync_to_async
	def get_guide(self,user):
		user = CustomUser.objects.get(id=user)
		return Guide.objects.get(user=user) or None


	@database_sync_to_async
	def is_guide(self, user_id):
		user = CustomUser.objects.get(id=user_id)
		if Guide.objects.filter(user=user).exists():
			return True
		else:
			return False


	@database_sync_to_async
	def get_chat_owner(self, chat_id):
		chat = Chat.objects.get(id=chat_id)
		return int(chat.user.id)



	@database_sync_to_async
	def get_user(self, user_id):
		return CustomUser.objects.get(id=user_id)

	@database_sync_to_async
	def get_chat(self, chat_id):
		return Chat.objects.get(id=chat_id)

	@database_sync_to_async
	def save_message(self, msg):
		msg.save()

	async def disconnect(self, close_code):
		pass
