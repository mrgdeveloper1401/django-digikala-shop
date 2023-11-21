"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


# admin rest 
admin_urls = [
    # accounts Admin
    path('accounts/admin/', include('accounts.admins.urls', namespace='account_admin')),
    # category admin
    path('Category/admin/', include('Category.admins.urls', namespace='category_admin')),
    # product admin
    path('products/admin/user/', include('products.admins.urls', namespace='products_admin_user')),
]
# client rest
client_urls = [
    # Category client
    path('category/client/', include('Category.client.urls', namespace='category_client')),
    # accounts client
    path('accounts/', include('accounts.clients.urls', namespace='account_client')),
    # products client
    path('products/', include('products.clients.urls', namespace='products_client')),
]
# swagger doc
open_api_doc = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
# jwt authentication credentials
jwt_token = [
    # jwt auth token
    path('api/token/generate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    # admin pannel
    path('store/', admin.site.urls),

] + client_urls + jwt_token + open_api_doc + admin_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'project shop'
admin.site.site_title = 'shop'