from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serialziers import UserSerialziers, profileSerializers, JobSerializers
from django.core import mail
from accounts.models import User, JobUserModel
from accounts.base_permission import IsOwner
from rest_framework.permissions import IsAuthenticated


class UserApiview(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialziers
    
    
class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = profileSerializers
    permission_classes = (IsOwner,)
    

class JobView(viewsets.ModelViewSet):
    queryset = JobUserModel.objects.all()
    serializer_class = JobSerializers
    permission_classes = (IsOwner, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
