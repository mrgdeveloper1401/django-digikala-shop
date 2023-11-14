from rest_framework import urls
from rest_framework.routers import DefaultRouter
from .views import UserCreateApiView
from django.urls import path, include

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')

app_name = 'account_client'
urlpatterns = [
    path('create_user/', UserCreateApiView.as_view(), name='create_user'),
    # path('', include(router.urls)),

]
# urlpatterns += router.urls