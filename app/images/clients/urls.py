from rest_framework.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import ImagesViewSet


router = DefaultRouter()
router.register(r'image', ImagesViewSet, basename='image')

app_name = 'images_client'
urlpatterns = [
    path('', include(router.urls))
] + router.urls
