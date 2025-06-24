from django.contrib import admin
from django.urls import path, include
from farmers.auth_views import urlpatterns as auth_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include("farmers.urls")),
    path('api/auth/', include(auth_urls)),
]
