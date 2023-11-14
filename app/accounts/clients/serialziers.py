from rest_framework import serializers
from accounts.models import User, JobUserModel


class UserSerialziers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = (
            'email',
            'mobile_phone',
            'password',
            'confirm_password',
            'first_name',
            'last_name'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            
        }
    
    def validate(self, value):
        if value['password']!= value['confirm_password']:
            raise serializers.ValidationError('password must mach')
        return value
    
    def create(self, validated_data):
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)
    
class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobUserModel
        fields = (
            'job',
            'user',
        )
    
    def create(self, validated_data):
        return JobUserModel.objects.create(**validated_data)

class profileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'mobile_phone',
            'birth_day',
            'last_login',
            'gender',
            'created_at',
        )