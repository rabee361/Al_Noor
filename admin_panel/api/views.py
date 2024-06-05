from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from base.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from django.db.models import Count
from django.db.models.functions import ExtractMonth








class LineChart(APIView):
    def get(self,request):
        year = datetime.now().year
        pilgrims = Pilgrim.objects.filter(created__year=year)\
                                        .annotate(month=ExtractMonth("created"))\
                                        .values("month").annotate(count=Count("id"))\
                                        .values("month", "count").order_by("month")
        serializer = ItemsPerMonthSerializer(pilgrims, many=True)
        return Response({
        "title": "الحجاج المسجلين حديثا",
        "data": {
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": '#FFFFFF',
                "borderColor": '#FFFFFF',
                "data": serializer.data,
            }]
        },
    })
    



class PieChart(APIView): 
    def get(self,request):
        completed_tasks = Task.objects.filter(completed=True).values("completed").aggregate(Count('id'))['id__count']
        remaining_tasks = Task.objects.filter(completed=False).values("completed").aggregate(Count('id'))['id__count']
        return Response({
            "completed":completed_tasks,
            "remaining":remaining_tasks
        })
