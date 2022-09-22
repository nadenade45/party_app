
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # mediaを使うために追加
from . import settings  # mediaを使うために追加

urlpatterns = [
   path('admin/', admin.site.urls),
   path('accounts/', include('allauth.urls')),  
   path('accounts/', include('accounts.urls')),  
   path('post/', include('post.urls')),
]

if settings.DEBUG:
   urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)  
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   