from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/User/', include('User.urls')),
    path('api/v1/Company/', include('Company.urls')),
    path('api/v1/Service/', include('Service.urls')),
    path('api/v1/Workers/', include('Workers.urls')),
    path('api/v1/Department/', include('Department.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
