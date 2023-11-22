from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import CommentModelViewSet, QuestionModelViewSet, AnswerProductModelViewSet


app_name = 'questions_client'
router = DefaultRouter()
router.register(r'question', CommentModelViewSet, basename='question')
router.register(r'question', QuestionModelViewSet, basename='question')
router.register(r'answer', AnswerProductModelViewSet, basename='answer')


urlpatterns = [
    path('', include(router.urls)),
] + router.urls
