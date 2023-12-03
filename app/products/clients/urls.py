from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import ProductViewSet, ProductLineViewSet, AttributeViewSet, AttributeValueViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'product_line', ProductLineViewSet, basename='product_line')
router.register(r'attribute', AttributeViewSet, basename='attribute')
router.register(r'attribute_value', AttributeValueViewSet, basename='attribute_value')

app_name = 'products_client'
urlpatterns = [
    path('', include(router.urls))
]
urlpatterns += router.urls
