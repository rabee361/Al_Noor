from rest_framework import serializers
from .models import * 
from .utils import weekday_mapping
from datetime import datetime







class HijriSerializer(serializers.Serializer):
    day = serializers.CharField()
    month = serializers.CharField()
    year = serializers.CharField()
    weekday = serializers.CharField()


class GregorianSerializer(serializers.Serializer):
    day = serializers.CharField()
    month = serializers.CharField()
    year = serializers.CharField()
