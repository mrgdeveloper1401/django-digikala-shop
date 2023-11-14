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
    birth_day = jmodels.jDateTimeField(_('تاریخ تولد'), blank=True, null=True)
    is_staff = models.BooleanField(_('کارمند'), default=False)
    is_active = models.BooleanField(_('فعال'), default=True)
    update_information = jmodels.jDateTimeField(_('update user'), auto_now=True)
    is_verified_email = models.BooleanField(_('تایید ایمیل'), default=False)
    is_verified_mmobile_phone = models.BooleanField(_('تایید شماره همراه'), default=False)
    last_login = jmodels.jDateTimeField(_('تاریخ اخرین ورود'), blank=True, null=True, default=timezone.now())

    class GenderChoose(models.TextChoices):
        female = 'female', _("Female")
        male = 'male', _("Male")
    gender = models.CharField(_('جنسیت'), max_length=6, choices=GenderChoose.choices, default=GenderChoose.male, blank=True)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'mobile_phone')

    objects = manager.UserManager()

    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')
        db_table = 'user'

class JobUserModel(CreateModel, UpdateModel):
    class JobChoose(models.TextChoices):
        sportman = 'sportman'
        historiology = 'historiology'
        socialـSciences = 'social Sciences'
        reporter = 'Reporter'
        lawyer = 'Lawyer'
        engineering  = 'Engineering'
        graphics = 'Graphics'
        marketing ='marketing'
        transportation = 'Transportation'
        programming = 'Programming'
        sales_marketing = 'Sales & Marketing'

    job = models.CharField(_('شغل'), max_length=17, choices=JobChoose.choices, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job')
    class Meta:
        verbose_name = _('شغل')
        verbose_name_plural = _('شغل ها')
        db_table = 'job'


class RecycleUser(User):
    deleted = Manager()

    class Meta:
        proxy = True
