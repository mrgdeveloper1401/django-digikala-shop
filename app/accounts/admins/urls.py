from rest_framework.urls import path
from rest_framework.urlpatterns import include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, JobUserViewSet

router = DefaultRouter()
router.register(r'user_admin', UserViewSet,basename='user admin')
router.register(r'job_user_admin', JobUserViewSet,basename='job user admin')

app_name = 'user_admin'
urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += router.urls