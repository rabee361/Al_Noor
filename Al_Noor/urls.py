from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('al-noor/admin/', admin.site.urls),
    path('al-noor/api/' , include('base.urls')),
    path('al-noor/myadmin/' , include('admin_panel.urls')),
    # path('al-noor/i18n/', include('django.conf.urls.i18n')),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

