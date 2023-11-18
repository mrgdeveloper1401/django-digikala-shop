from rest_framework import viewsets
from accounts.models import User, JobUserModel
from .serialziers import UserSerializer, JobUserSerializer
from accounts.base_permission import IsSuperUser, IsOwner
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


class JobUserViewSet(viewsets.ModelViewSet):
    queryset = JobUserModel.objects.all()
    serializer_class = JobUserSerializer
    permission_classes = (IsSuperUser,)
    

