from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('wifi_checker', include('wifi_checker.urls')),
    path('covid_checker', include('covid_checker.urls')),
    path('dust_checker', include('dust_checker.urls')),
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)