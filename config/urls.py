from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщина мира"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)