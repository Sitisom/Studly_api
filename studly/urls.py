from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from studly import settings

urlpatterns = [
    path('core/', include('core.urls')),
    path('auth/', include('auth.urls')),
    path('lesson/', include('lessons.urls')),
    path('course/', include('course.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
