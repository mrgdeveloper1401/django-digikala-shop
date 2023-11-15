from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SallerProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'saller', SallerProductViewSet, basename='saller')
app_name = 'products_admin_user'
urlpatterns = [
    
]
urlpatterns += router.urls
