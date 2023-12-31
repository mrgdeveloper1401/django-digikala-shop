from rest_framework import urls
from rest_framework.routers import DefaultRouter
from .views import UserApiview, ProfileView, JobView
from django.urls import path, include

router = DefaultRouter()
router.register(r'job', JobView, basename='job')
# router.register(r'users', UserApiview, basename='users')

app_name = 'account_client'
urlpatterns = [
    path('create_user/', UserApiview.as_view(), name='create_user'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),

]
urlpatterns += router.urls