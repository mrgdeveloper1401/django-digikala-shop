from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .viesw import GenuinSallerViewSet


router = DefaultRouter()
router.register(r'genuinsaller', GenuinSallerViewSet, basename='genuian')

app_name = 'sallers'
urlpatterns = [
    path('', include(router.urls)),
] + router.urls
