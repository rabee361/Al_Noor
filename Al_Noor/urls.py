from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('test/admin/', admin.site.urls),
    path('test/api/' , include('base.urls')),
    path('test/admin/' , include('admin_panel.urls')),
    path('test/myapi/' , include('admin_panel.api.urls')),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

urlpatterns += [path('test/silk/', include('silk.urls', namespace='silk'))]
