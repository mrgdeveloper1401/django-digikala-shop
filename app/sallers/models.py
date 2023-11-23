from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel
from location_field.models.plain import PlainLocationField


# class JobSaller(models.Model):
#     class JaboChoose(models.TextChoices):
#         employee = ('employee'), _('کارمند')
#         owener_bussiness = ('owener bussiness'), _('کسب و کار شخصی')
#         freelance_job = ('freelance job'), _('شغل آزاد')
#         retired = ('retired'), _('بازنشسته')
#         other = ('other'), _('سایر')
#     job = models.CharField(_('شغل اصلی'), max_length=16)

#     def __str__(self) -> str:
#         return self.job
    
#     class Meta:
#         verbose_name = _('job saller')
#         verbose_name_plural = _('job sallers')
#         db_table = 'job_saller'


class LocationModel(CreateModel, UpdateModel):
    state = models.CharField(_('شهرستان'), max_length=100)
    city = models.CharField(_('شهر'), max_length=100)
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True, null=True)
    plaque = models.CharField(_('پلاک'), max_length=11, blank=True, null=True)
    postacl_code = models.CharField(_('کد پستی'), max_length=11)

    def __str__(self) -> str:
        return f"{self.city}, {self.state}"
    
    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        db_table = 'location'


class Multiplehoose(models.Model):
    name = models.CharField(_('متن سوال'), max_length=50, db_index=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'multiple option'
        verbose_name_plural = 'multiple options'
        db_table = 'multiple_option'


class MultipleChooseAttribute(models.Model):
    question = models.ForeignKey(Multiplehoose, on_delete=models.CASCADE, related_name='multiple_question')
    text_option = models.CharField(_('گزینه سوال'), max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.text_option
    
    class Meta:
        verbose_name = 'multiple choose'
        verbose_name_plural = 'multiple choiceses'
        db_table = 'multiple_choose_atrribute'


class GenuinSaller(CreateModel, UpdateModel):
    nation_code = models.CharField(_('کد ملی'), max_length=10,
                                   help_text='max length 10 characters')
    card_number = models.CharField(_('شماره کارت بانکی'), max_length=16, unique=True,
                                   help_text='0000-0000-0000-0000', blank=True, null=True)
    sheba_number = models.CharField(_('شماره شبای  بانکی'), max_length=24, unique=True,
                                    help_text='IR-000000000000000000000000', blank=True, null=True)
    shop_name = models.CharField(_('نام فروشگاه'), max_length=50, unique=True, db_index=True,
                                 help_text='excample azarakhs, ...')
    
    def __str__(self) -> str:
        return self.shop_name

    class Meta:
        verbose_name = _('saller')
        verbose_name_plural = _('sellers')
        db_table ='genuin_saller'


class SignatoryModel(CreateModel, UpdateModel):
    name = models.CharField(_('امضا کننده مالک شرکت'), max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('signatory')
        verbose_name_plural = _('signatories')


class legalSaller(CreateModel, UpdateModel):
    company_name = models.CharField(_('نام شرکت'), max_length=50)
    nation_code_company = models.CharField(_('کد ملی شرکت'), max_length=11)
    economy_code_company = models.CharField(_('کد اقتصادی شرکت'), max_length=12)
    sheba_number = models.CharField(_('شماره شبای  بانکی'), max_length=24, unique=True,
                                    help_text='IR-000000000000000000000000')
    company_owner_signatory = models.ForeignKey(SignatoryModel, on_delete=models.PROTECT, related_name='signatories')

    def __str__(self) -> str:
        return self.company_name
    
    class Meta:
        verbose_name = _('legal saller')
        verbose_name_plural = _('legal sellers')
        db_table = 'legal_saller'