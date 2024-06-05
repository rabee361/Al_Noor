from django.urls import path
from .views import *


urlpatterns = [
    path('chart/line-chart/', LineChart.as_view() , name="line-chart"),
    path('chart/pie-chart/' , PieChart.as_view() , name="pie-chart"),
]
