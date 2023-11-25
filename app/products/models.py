from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel
from .Fields import OrderFields


class ProductAttributeModel(CreateModel, UpdateModel):
    attr = models.CharField(max_length=50, db_index=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.attr
    
    class Meta:
        verbose_name = _('product attribute')
        verbose_name_plural = _('product attrobutes')
        db_table = 'product_attribute'


class ProductAttributeValueModel(CreateModel, UpdateModel):
    attr_value = models.CharField(max_length=50, blank=True)
    attribute = models.ForeignKey(ProductAttributeModel, on_delete=models.CASCADE, related_name='attributes')
    
    def __str__(self) -> str:
        return self.attr_value
    
    class Meta:
        verbose_name = _('product attribute value')
        verbose_name_plural = _('product attribute values')
        db_table = 'product_attribute_value'


class ProductLineAttributeValueModel(CreateModel, UpdateModel):
    attr_values = models.ForeignKey(ProductAttributeValueModel, on_delete=models.CASCADE, related_name='pro_attr_values')
    product_line = models.ForeignKey('ProductLineModel', on_delete=models.CASCADE, related_name='pro_line_attr_values')
    attribute_model = models.ForeignKey(ProductAttributeModel, on_delete=models.CASCADE)  # این خط اضافه شده است

    def __str__(self) -> str:
        return self.attr_values.attr_value
    
    class Meta:
        unique_together = (('attr_values', 'product_line'),)
        verbose_name = _('product line attribute value')
        verbose_name_plural = _('product line attribute values')

class BrandModel(CreateModel, UpdateModel):
    brand_name = models.CharField(_('نام برند'), max_length=100, unique=True)
    slug = models.SlugField(max_length=100, allow_unicode=True)
    
    def __str__(self) -> str:
        return self.brand_name
    
    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')
        db_table = 'brand'


class ProductLineModel(CreateModel, UpdateModel):
    upc = models.CharField(_('بارکد'), max_length=20, unique=True)
    sku = models.CharField(_('بارکد اختصاصی انبارداری'), max_length=50, unique=True)
    price = models.DecimalField(_('قیمت کالا'), decimal_places=3, max_digits=12)
    is_stock = models.BooleanField(_("موجود هست"), default=True)
    is_delivery = models.BooleanField(_("ارسال از طریق پست"), default=True)
    number_product = models.PositiveSmallIntegerField(_("تعداد محصول"))
    is_active = models.BooleanField(default=True)
    attribute_value = models.ManyToManyField(ProductAttributeModel, through='ProductLineAttributeValueModel')
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE, related_name='products')
    
    def __str__(self) -> str:
        return self.upc

    class Meta:
        verbose_name = _('product line')
        verbose_name_plural = _('product lines')
        db_table = 'product_line'


class ProductModel(CreateModel, UpdateModel):
    saller = models.ForeignKey('sallers.GenuinSaller', on_delete=models.CASCADE, related_name='sallers')
    category = models.ForeignKey('Category.Category', on_delete=models.PROTECT, related_name='categories')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='brands')
    product_name = models.CharField(_('نام کالا'), max_length=150, db_index=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=150)
    description_product = models.TextField(_("معرفی کالا"), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.product_name

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'product'
