from rest_framework import serializers
from base.models import *
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
        )
        user.set_password('lkdsjlkfdjsl')
        user.save()
        pilgrim = Pilgrim.objects.create(first_name=first_name, family_name=family_name, user=user, phonenumber=phonenumber, **validated_data)
        return pilgrim
    

class TypeGuidanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGuidance
        fields = '__all__'

class ReligiousGuideSerializer(serializers.ModelSerializer):
    type_guidance = serializers.CharField(read_only=True)

    class Meta:
        model = ReligiousGuide
        fields = '__all__'

    def create(self, validated_data):
        type_guidance = self.context.get('type_guidance')
        instance = ReligiousGuide.objects.create(type_guidance=type_guidance, **validated_data)
        return instance
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['type_guidance'] = instance.type_guidance.name
        return repr
    
class TypeReligiousSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeReligious
        fields = '__all__'

class ReligiousWorksSerializer(serializers.ModelSerializer):

    type_religious = serializers.CharField(read_only=True)
    class Meta:
        model = ReligiousWorks
        fields = '__all__'

    def create(self, validated_data):
        type_religious = self.context.get('type_religious')
        instance = ReligiousWorks.objects.create(type_religious=type_religious, **validated_data)
        return instance
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['type_religious'] = instance.type_religious.name
        return repr