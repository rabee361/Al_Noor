
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('al-noor/admin/', admin.site.urls),
    path('al-noor/api/' , include('base.urls')),
    path('al-noor/myadmin/' , include('admin_panel.urls'))
]
