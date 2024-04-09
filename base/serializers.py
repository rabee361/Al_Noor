from rest_framework import serializers
from .models import *
class PilgrimSeriailzer(serializers.ModelSerializer):

    class Meta:
        model = Pilgrim

        # fields = '__all__'
        exclude = ['user',]

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        family_name = validated_data.pop('family_name')
        phonenumber = validated_data.pop('phonenumber')
        user = CustomUser.objects.create(
            username = f'{first_name} {family_name}',
            phonenumber = phonenumber,
            password = 'sdjflasjdlfja'
        )
        pilgrim = Pilgrim.objects.create(first_name=first_name, family_name=family_name, user=user, **validated_data)
        return pilgrim