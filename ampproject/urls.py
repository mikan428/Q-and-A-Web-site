
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path , include
from django.conf.urls.static import static
from . import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ampapp.urls')),
   
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)