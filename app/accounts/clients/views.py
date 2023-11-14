from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from accounts.models import User, JobUserModel
from .serialziers import UserSerialziers
from rest_framework.response import Response
from rest_framework import status
from django.core import mail


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialziers
    
    