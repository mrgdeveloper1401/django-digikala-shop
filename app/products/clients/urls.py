from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import ProductViewSet, ProductLineViewSet, ProductImageViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'product_line', ProductLineViewSet, basename='product_line')
router.register(r'product_image', ProductImageViewSet, basename='product_line_image')


app_name = 'products_client'
urlpatterns = [
    path('', include(router.urls))
] + router.urls
