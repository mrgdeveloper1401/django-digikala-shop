from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from django.db.models import Manager
from .manager import UserManager
from common.models import SoftDelete, CreateModel, UpdateModel
from django.utils import timezone
    

class User(AbstractBaseUser, PermissionsMixin, SoftDelete, CreateModel, UpdateModel):
    email = models.EmailField(max_length=100, unique=True)
    mobile_phone = models.CharField(unique=True,max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_day = jmodels.jDateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified_email = models.BooleanField(default=False)
    is_verified_mmobile_phone = models.BooleanField(default=False)
    last_login = jmodels.jDateTimeField(blank=True, null=True, default=timezone.now())
    nation_code = models.CharField(max_length=10, blank=True, null=True,
                                   help_text='max length 10 characters', unique=True)
    
    class GenderChoose(models.TextChoices):
        female = 'female'
        male = 'male'
    gender = models.CharField(max_length=6, choices=GenderChoose.choices, default=GenderChoose.male, blank=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'mobile_phone')

    def __str__(self) -> str:
        return self.email
    
    objects = UserManager()

    class Meta:
        db_table = 'user'


class UserProxy(User):
    class Meta:
        proxy = True


class JobUserModel(CreateModel, UpdateModel):
    class JobChoose(models.TextChoices):
        IT = 'IT'
        FINANCIAL_ACCOUNTING = 'financial accounting'
        SALE_MARKETING = 'sale marketing'
        HEALTH_MEDICINE = 'health medical'
        EDUCATION_TRAINING = 'education training'
        ENGINEER_CONSTRACTION = 'engineer construction'
        ART_DESIGN = 'art design'
        RESTAURENT_FOOD_SERVICES = 'restaurant food services'
        COMMERCIAL_LEGAL = 'commercial legal'
        ENVIRONMENT_SUSTAINABLITY = 'environment sustainability'
    job = models.CharField(max_length=26, choices=JobChoose.choices, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job')
    
    def __str__(self) -> str:
        return f'{self.user.email} -- {self.job}'
    
    class Meta:
        db_table = 'job'


class LegalUser(User):
    organization_name = models.CharField(max_length=100)
    economy_code = models.CharField(max_length=12, help_text='max length 12 characters', unique=True)
    nation_code_organization = models.CharField(max_length=11, help_text='max length 11 characters', unique=True)
    state_name = models.CharField(max_length=50,blank=True, null=True)
    city_name = models.CharField(max_length=10, blank=True, null=True)
    landing_phone = models.CharField(max_length=11)
    is_enable = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.organization_name
    
    class Meta:
        db_table = 'legal_user'


class RecycleUser(User):
    deleted = Manager()

    class Meta:
        proxy = True


class RecycleLegalUser(LegalUser):
    deleted = Manager()

    class Meta:
        proxy = True
