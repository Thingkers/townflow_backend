from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

def health_check(request):
    return JsonResponse({'status': 'ok', 'message': 'Django is running!'})

urlpatterns = [
    # Admin Interface
    path("admin/", admin.site.urls),
    
    # Server Monitoring
    path("health/", health_check, name="health"),
    
    # API Documentation Engines
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    
    # 🌟 THIS LINKS YOUR API PATH TO YOUR APP CODE 🌟
    path("api/v1/", include("config.v1_urls")),
]

# Asset Management
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)