from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serialziers import UserSerialziers, profileSerializers, JobSerializers
from django.core import mail
from accounts.models import User, JobUserModel
from accounts.base_permission import IsOwner


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialziers
    
    
class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = profileSerializers
    permission_classes = (IsOwner,)
    

class JobView(viewsets.ViewSet):
    permission_classes = (IsOwner, )
    
    def create(self, request):
        ser_data = JobSerializers(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        job = get_object_or_404(JobUserModel, pk=pk)
        ser_data = JobSerializers(job, data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)