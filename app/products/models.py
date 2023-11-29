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
        db_table = 'product_attribute'


class ProductAttributeValueModel(CreateModel, UpdateModel):
    attr_value = models.CharField(max_length=50, blank=True)
    attribute = models.ForeignKey(ProductAttributeModel, on_delete=models.CASCADE, related_name='attributes')
    
    def __str__(self) -> str:
        return self.attr_value
    
    class Meta:
        db_table = 'product_attribute_value'


class ProductLineAttributeValueModel(CreateModel, UpdateModel):
    attribute = models.ForeignKey(ProductAttributeModel, on_delete=models.CASCADE, related_name='throught_attribute')
    attribute_value = models.ForeignKey(ProductAttributeValueModel, on_delete=models.CASCADE, related_name='throught_attribute_value')
    product_line = models.ForeignKey('ProductLineModel', on_delete=models.CASCADE, related_name='pro_line_attr_values')

    def __str__(self) -> str:
        return self.attr_values.attr_value
    
    class Meta:
        unique_together = (('attribute', 'attribute_value'),)


class ProductLineModel(CreateModel, UpdateModel):
    upc = models.CharField(max_length=20, unique=True)
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(decimal_places=3, max_digits=12)
    is_stock = models.BooleanField(default=True)
    is_delivery = models.BooleanField(default=True)
    number_product = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    attribute_value = models.ManyToManyField(ProductAttributeModel, through='ProductLineAttributeValueModel')
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE, related_name='products')
    product_type = models.ForeignKey('ProductTypeModel', on_delete=models.CASCADE, related_name='product_line_types')
    
    def __str__(self) -> str:
        return self.upc

    class Meta:
        db_table = 'product_line'

class ProductTypeModel(CreateModel, UpdateModel):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class ProductTypeAttributeModel(CreateModel, UpdateModel):
    product_type = models.ForeignKey(ProductTypeModel, on_delete=models.CASCADE, related_name='product_types')
    attribute = models.ForeignKey(ProductAttributeModel, on_delete=models.CASCADE, related_name='product_type_attribute')

    class Meta:
        unique_together = ('product_type', 'attribute')


class BrandModel(CreateModel, UpdateModel):
    brand_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, allow_unicode=True)
    
    def __str__(self) -> str:
        return self.brand_name
    
    class Meta:
        db_table = 'brand'


class ProductModel(CreateModel, UpdateModel):
    saller = models.ForeignKey('sallers.GenuinSaller', on_delete=models.CASCADE, related_name='sallers')
    category = models.ForeignKey('Category.Category', on_delete=models.PROTECT, related_name='categories')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='brands')
    product_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=150)
    description_product = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.product_name

    class Meta:
        db_table = 'product'
