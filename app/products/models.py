from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from common.fields import UpperCharField
from common.models import CreateModel, UpdateModel
from .exception import Deplicated


class Option(CreateModel):
    title = models.CharField(_('عنوان'), max_length=50, db_index=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')
        db_table = 'option'
        

class ProductAttributeModel(models.Model):
    title = models.CharField(_('عنوان ویژگی'), max_length=50, db_index=True)
    product = models.ForeignKey('ProductModel', on_delete=models.PROTECT, related_name='pro_attr')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('product attribute')
        verbose_name_plural = _('product attrobutes')
        db_table = 'product_attribute'
        

class ProductAttributeValueModel(models.Model):
    title = models.CharField(_('ویژگی'), max_length=50, blank=True)
    product = models.ForeignKey('ProductModel', on_delete=models.PROTECT, related_name='pro_attr_value')

    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('product attribute value')
        verbose_name_plural = _('product attribute values')
        db_table = 'product_attribute_value'


class ProductLine(CreateModel, UpdateModel):
    upc = models.CharField(_('بارکد'), max_length=20, unique=True)
    sku = models.CharField(_('بارکد اختصاصی انبارداری'), max_length=50, unique=True)
    price = models.DecimalField(_('قیمت کالا'), decimal_places=3, max_digits=12)
    is_stock = models.BooleanField(_("موجود هست"), default=True)
    is_delivery = models.BooleanField(_("ارسال از طریق پست"), default=True)
    number_product = models.PositiveSmallIntegerField(_("تعداد محصول"))
    is_active = models.BooleanField(default=True)
    product_line = models.ForeignKey('ProductModel', on_delete=models.PROTECT, related_name='product_lines')

    def __str__(self) -> str:
        return self.upc

    class Meta:
        verbose_name = _('جزییات محصول')
        verbose_name_plural = _('جزییات محصولات')
        db_table = 'product_line'


class ProductModel(CreateModel, UpdateModel):
    saller = models.ForeignKey('SallerModel', on_delete=models.PROTECT, related_name='sallers')
    category = models.ForeignKey('Category.Category', on_delete=models.PROTECT, related_name='categories')
    product_name = models.CharField(_('نام کالا'), max_length=150, db_index=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=150)
    description_product = models.TextField(_("معرفی کالا"), blank=True, null=True)
    image = models.ForeignKey('images.ImagesModel', on_delete=models.PROTECT, related_name='product_images')
    options = models.ManyToManyField(Option, blank=True)
    is_active = models.BooleanField(default=True)

    class Warrentychoose(models.TextChoices):
        no_warrenty = 'no warrenty', _('no warrenty')
        company_warrenty = 'company warrenty', _('company warrenty')
    warrenty_choose = models.CharField(_('نوع گارانتی'), max_length=16, choices=Warrentychoose.choices, default=Warrentychoose.no_warrenty)
    company_warrent_name = models.CharField(_('نام شرکت گارانتی کننده'), max_length=50, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.product_name

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'product'
        

class SallerModel(CreateModel, UpdateModel):
    company_name = models.CharField(_('اسم تولیدی'), max_length=50)
    slug = models.SlugField(allow_unicode=True, unique=True)
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='users')
    province_name = models.CharField(_('استان'), max_length=50)
    eprachy_name = models.CharField(_('شهرستان'), max_length=50)
    city = models.CharField(_('شهر'), max_length=50)
    address = models.TextField(_('ادرس'))
    postacl_code = models.CharField(_('آدرس پستی تولیدی'), max_length=11, unique=True)
    
    def __str__(self) -> str:
        return self.company_name

    class Meta:
        verbose_name = _('saller')
        verbose_name_plural = _('sellers')
        db_table ='saller'
