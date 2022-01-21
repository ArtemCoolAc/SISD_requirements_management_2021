from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('requirements/', include('requirements.urls')),
    path('specifications/', include('specifications.urls')),
    path('releases/', include('releases.urls')),
    path('projects/', include('projects.urls')),
    path('auth/', include('authorization.urls')),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
