from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from admin_panel.views import PilgrimFormView , LandinPageView 


urlpatterns = [
    path('supersecureadmin/', admin.site.urls),
    path('api/' , include('base.urls')),
    path('admin/' , include('admin_panel.urls')),
    path('myapi/' , include('admin_panel.api.urls')),
    path('' , LandinPageView.as_view() , name="welcome"),
    path('form/' , PilgrimFormView.as_view() , name="form"),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
