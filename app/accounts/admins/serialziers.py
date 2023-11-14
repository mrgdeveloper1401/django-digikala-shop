from accounts.models import User, JobUserModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class JobUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobUserModel
        fields = '__all__'