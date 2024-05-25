from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('test/admin/', admin.site.urls),
    path('test/api/' , include('base.urls')),
    path('test/myadmin/' , include('admin_panel.urls')),
    # path('test/', include('django_prometheus.urls')),
    # path('al-noor/i18n/', include('django.conf.urls.i18n')),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

urlpatterns += [path('test/silk/', include('silk.urls', namespace='silk'))]
