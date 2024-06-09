from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , include('base.urls')),
    path('myadmin/' , include('admin_panel.urls')),
    path('myapi/' , include('admin_panel.api.urls')),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
