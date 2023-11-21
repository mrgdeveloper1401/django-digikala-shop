from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from django.db.models import Manager
from . import manager
from common.models import SoftDelete, CreateModel, UpdateModel
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin, SoftDelete, CreateModel, UpdateModel):
    email = models.EmailField(_('ایمیل'),max_length=100, unique=True)
    mobile_phone = models.CharField(_('شماره همراه'), unique=True,max_length=11)
    first_name = models.CharField(_('نام'), max_length=100)
    last_name = models.CharField(_('خانوادگی'), max_length=100)
    birth_day = jmodels.jDateField(_('تاریخ تولد'), blank=True, null=True)
    is_staff = models.BooleanField(_('کارمند'), default=False)
    is_active = models.BooleanField(_('فعال'), default=True)
    is_verified_email = models.BooleanField(_('تایید ایمیل'), default=False)
    is_verified_mmobile_phone = models.BooleanField(_('تایید شماره همراه'), default=False)
    last_login = jmodels.jDateTimeField(_('تاریخ اخرین ورود'), blank=True, null=True, default=timezone.now())
    nation_code = models.CharField(_('کد ملی'), max_length=10, blank=True, null=True,
                                   help_text='max length 10 characters', unique=True)
    
    class GenderChoose(models.TextChoices):
        female = 'female', _("زن")
        male = 'male', _("مرد")
    gender = models.CharField(_('جنسیت'), max_length=6, choices=GenderChoose.choices, default=GenderChoose.male, blank=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'mobile_phone')

    def __str__(self) -> str:
        return self.email
    
    objects = manager.UserManager()

    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')
        db_table = 'user'

class JobUserModel(CreateModel, UpdateModel):
    class JobChoose(models.TextChoices):
        IT = 'IT', _("فناوری و اطلاعات")
        FINANCIAL_ACCOUNTING = 'financial accounting', _('مالی و حسابداری')
        SALE_MARKETING = 'sale marketing', _('مالی و حسابداری')
        HEALTH_MEDICINE = 'health medical', _('سلامت و پزشکی')
        EDUCATION_TRAINING = 'education training', _('فروش و بازاریابی')
        ENGINEER_CONSTRACTION = 'engineer construction', _('آموزش و تربیت')
        ART_DESIGN = 'art design', _('مهندسی و ساخت')
        RESTAURENT_FOOD_SERVICES = 'restaurant food services', _('خدمات رستورانی و غذایی')
        COMMERCIAL_LEGAL = 'commercial legal', _('بازرگانی و حقوق')
        ENVIRONMENT_SUSTAINABLITY = 'environment sustainability', _('محیط زیست و پایداری')
    job = models.CharField(_('شغل'), max_length=26, choices=JobChoose.choices, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job')
    
    def __str__(self) -> str:
        return f'{self.user.email} -- {self.job}'
    
    class Meta:
        verbose_name = _('شغل')
        verbose_name_plural = _('شغل ها')
        db_table = 'job'


class RecycleUser(User):
    deleted = Manager()

    class Meta:
        verbose_name = _('کاربر پاک شده')
        verbose_name_plural = _('کاربران پاک شده')
        proxy = True
