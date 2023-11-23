from django.urls import include
from rest_framework.urls import path
from .views import OptionModelViewSet, ProductAttributeModelViewSet \
    ,ProductLineModelViewSet, ProductModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'option', OptionModelViewSet, basename='option')
router.register(r'product_attribute', ProductAttributeModelViewSet, basename='product_attribute')
router.register(r'product_line', ProductLineModelViewSet, basename='product_line')
router.register(r'product', ProductModelViewSet, basename='product')

app_name = 'products'
urlpatterns = [
    path('', include(router.urls)),
] + router.urls
