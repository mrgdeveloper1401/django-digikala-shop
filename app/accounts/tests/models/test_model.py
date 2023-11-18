import factory
from accounts.models import User, JobUserModel
from django.utils import timezone

class UserFactory(factory.Factory):
    class Meta:
        model = User
        
    email = 'm.goodarzi606@gmail.com'
    mobile_phone = '09210514437'
    first_name = 'mohammad'
    last_name = 'goodarzi'
    birth_day = '1379-07-30'
    is_staff = False
    is_active = True
    is_superuser = False
    is_verified_email = False
    is_verified_mmobile_phone = False
    last_login = timezone.now()
    password = 'user.1234'
    is_deleted = False
    deleted_at = None
    update_at = timezone.now()
    created_at = timezone.now()
    
    