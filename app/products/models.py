from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from common.fields import UpperCharField


class OptionGroup(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Option Group"
        verbose_name_plural = "Option Groups"


class OptionGroupValue(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE,
                              related_name='groups')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Option Group Value"
        verbose_name_plural = "Option Group Values"
        

class ProductClass(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=2048, null=True, blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    track_stock = models.BooleanField(default=True)
    require_shipping = models.BooleanField(default=True)
    options =  models.ManyToManyField('Option', blank=True)
    
    @property
    def has_attribute(self):
        return self.attributes.exists()

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Product Class"
        verbose_name_plural = "Product Classes"
        

class ProductAttribute(models.Model):
    class AttributeTypeChoice (models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option  = 'option'
        multi_option = 'multi_option'

    product_class =  models.ForeignKey(ProductClass, on_delete=models.CASCADE, null=True, related_name='attributes')
    title = models.CharField(max_length=64)
    type  = models.CharField(max_length=16, choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.text)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null=True, blank=True)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Product Attribute"
        verbose_name_plural = "Product Attributes"
    
    
class Option(models.Model):
    class OptionTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option = 'option'
        multi_option = 'multi_option'

    title = models.CharField(max_length=64)
    type = models.CharField(max_length=16, choices=OptionTypeChoice.choices, default=OptionTypeChoice.text)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null=True, blank=True,
                                     related_name='option_groups')
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Product(models.Model):
    class ProductTypeChoice(models.TextChoices):
        standalone = 'standalone'
        parent = 'parent'
        child = 'child'

    structure = models.CharField(max_length=16, choices=ProductTypeChoice.choices, default=ProductTypeChoice.standalone)
    parent = models.ForeignKey("self", related_name="children", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    upc = UpperCharField(max_length=24, unique=True, null=True, blank=True)
    is_public = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=128, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    product_class = models.ForeignKey(on_delete=models.PROTECT, null=True, blank=True,related_name='products')
    attribute = models.ManyToManyField(ProductAttribute)

    slug = models.SlugField(unique=True, allow_unicode=True)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"