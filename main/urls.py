from . import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', include('main_page.urls')),
    path('tags/', include('tags.urls')),
    path('basket/', include('basket.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)