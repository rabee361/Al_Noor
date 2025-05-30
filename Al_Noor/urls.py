from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from admin_panel.views import PilgrimFormView , LandinPageView , TermsandConditionsView , PilgrimFormSigninView , limit_reached


urlpatterns = [
    path('supersecureadmin/', admin.site.urls),
    path('api/' , include('base.urls')),
    path('admin/' , include('admin_panel.urls')),
    path('myapi/' , include('admin_panel.api.urls')),
    path('' , LandinPageView.as_view() , name="welcome"),
    path('form/' , limit_reached.as_view() , name="form"),
    # path('form/signin/' , PilgrimFormSigninView.as_view() , name="form"),
    path('terms/' , TermsandConditionsView.as_view() , name="terms"),
    path('silk/', include('silk.urls', namespace='silk'))

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

