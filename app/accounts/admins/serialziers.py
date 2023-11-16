from accounts.models import User, JobUserModel
from rest_framework import serializers



class JobUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobUserModel
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobUserModel
        fields = ('job', )

class UserSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    class Meta:
        model = User
        fields = '__all__'
