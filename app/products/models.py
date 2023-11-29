from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel
from .Fields import OrderFields


class OptionGroup(CreateModel, UpdateModel):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'option_groups'


class ProductLineModel(CreateModel, UpdateModel):
    title_productLine = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True)
    description = models.TextField(help_text='explain description product')
    require_shipping = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title_productLine

    class Meta:
        db_table = 'product_line'


class ProductModel(CreateModel, UpdateModel):
    class ProductStructre(models.TextChoices):
        standallowne = 'standalone'
        parent = 'parent'
        child = 'child'
    structure = models.CharField(max_length=12, choices=ProductStructre.choices, default=ProductStructre.standallowne)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='parents')
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True)
    upc = models.CharField(max_length=24, unique=True, blank=True, null=True)
    is_public = models.BooleanField(default=False)
    product_line = models.ForeignKey(ProductLineModel, on_delete=models.PROTECT, related_name='product_classes')
    category = models.ForeignKey('category.Category', on_delete=models.PROTECT, related_name='product_categories')
    
    def __str__(self) -> str:
        return self.product_name

    class Meta:
        db_table = 'product'


class ProductAttributeModel(CreateModel, UpdateModel):
    class AttributeTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        dateetime = 'datetime'
        option = 'option'
        multi_option = 'multi_option'
    types = models.CharField(max_length=12, choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.text)
    attribute_title = models.CharField(max_length=50)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, related_name='option_groups')
    product_line = models.ForeignKey(ProductLineModel, on_delete=models.PROTECT, related_name='product_lines')
    
    def __str__(self) -> str:
        return self.attribute_title
    
    class Meta:
        db_table = 'product_attribute'
        
        
class ProductAttributeValueModel(CreateModel, UpdateModel):
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT, related_name='products')
    product_attribute = models.ForeignKey(ProductAttributeModel, on_delete=models.PROTECT, related_name='product_attributes')
    value_text = models.TextField()
    value_integer = models.IntegerField()
    value_float = models.FloatField()
    value_datetime = models.DateTimeField()
    value_date = models.DateField()
    
    
    def __str__(self) -> str:
        return self.product.product_name
    
    class Meta:
        db_table = 'product_attribute_value'