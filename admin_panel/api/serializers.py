from rest_framework import serializers
import calendar




class ItemsPerMonthSerializer(serializers.Serializer):
    month_name = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    def get_month_name(self, obj):
        return calendar.month_name[obj['month']]