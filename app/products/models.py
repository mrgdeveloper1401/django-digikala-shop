from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from common.fields import UpperCharField
from common.models import CreateModel, UpdateModel


class Option(CreateModel):
    title = models.CharField(_('عنوان'), max_length=50, db_index=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')
        db_table = 'option'
        

class OptionValueModel(models.Model):
    title = models.CharField(_('عنوان'), max_length=50, db_index=True)
    body_option_value = models.CharField(_("متن عنوان"), max_length=100)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('option value')
        verbose_name_plural = _('option values')
        db_table = 'option_value'
        

class ProductModel(CreateModel):
    category = models.OneToOneField('Category.Category', on_delete=models.PROTECT, related_name='categories')
    product_name = models.CharField(_('نام کالا'), max_length=150, db_index=True)
    price = models.PositiveIntegerField(_('قیمت'), db_index=True)
    description_product = models.TextField(blank=True, null=True)
    barcode = models.PositiveBigIntegerField(_('بارکد کالا'))
    product_auth_code = models.CharField(_('کد شناسایی هر کالا'), max_length=128, unique=True)
    option = models.ManyToManyField(Option, related_name='options',)
    saller = models.ForeignKey('SallerModel', on_delete=models.PROTECT, related_name='sallers')
    image = models.ManyToManyField('images.ImagesModel', related_name='product_images')
    is_stock = models.BooleanField(_("موجود هست"), default=True)
    number_product = models.PositiveSmallIntegerField(_("تعداد محصول"))
    is_delivery = models.BooleanField(_("ارسال از طریق پست"), default=True)
    
    class Warrentychoose(models.TextChoices):
        no_warrenty = 'no warrenty', _('no warrenty')
        company_warrenty = 'company warrenty', _('company warrenty')
    warrenty_choose = models.CharField(_('نوع گارانتی'), max_length=16, choices=Warrentychoose.choices, default=Warrentychoose.no_warrenty)
    
    def __str__(self) -> str:
        return self.title_product.product_name

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'product'
        
        
class SallerModel(CreateModel, UpdateModel):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='users')
    company_name = models.CharField(_('اسم تولیدی'), max_length=50)
    province_name = models.CharField(_('استان'), max_length=50)
    eprachy_name = models.CharField(_('شهرستان'), max_length=50)
    city = models.CharField(_('شهر'), max_length=50)
    address = models.TextField(_('ادرس'))
    postacl_code = models.CharField(_('کد پستی'), max_length=11, unique=True)
    nation_code = models.CharField(_('کد ملی'), max_length=11, unique=True)
    
    
    def __str__(self) -> str:
        return self.company_name

    class Meta:
        verbose_name = _('saller')
        verbose_name_plural = _('sellers')
        db_table ='saller'
