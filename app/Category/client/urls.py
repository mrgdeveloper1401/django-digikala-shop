from django.urls import include
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from .veiws import CategoryViewSet, BrandViewSet


router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'brand', BrandViewSet, basename='brand')

app_name = 'category_client'
urlpatterns = [
    path('', include(router.urls)),
] + router.urls
