from rest_framework import viewsets
from accounts.models import User, JobUserModel
from .serialziers import UserSerializer, JobUserSerializer
from accounts.base_permission import IsSuperUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


class JobUserViewSet(viewsets.ModelViewSet):
    queryset = JobUserModel.objects.all()
    serializer_class = JobUserSerializer
    permission_classes = (IsSuperUser,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
