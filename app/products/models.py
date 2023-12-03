from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel


# product line model
class ProductLine(CreateModel, UpdateModel):
    price = models.DecimalField(decimal_places=3, max_digits=12)
    sku = models.CharField(max_length=24, unique=True, blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_publish = models.BooleanField(default=True)
    attribute_value = models.ManyToManyField("AttributeValue", related_name="product_line_attribute_value", through='ProductLineAttributeValue')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='product_line_products')

    def __str__(self) -> str:
        return self.product.product_name

    class Meta:
        db_table = 'product_line'


# product model
class Product(CreateModel, UpdateModel):
    class ProductStructre(models.TextChoices):
        standalone = 'standalone'
        parent = 'parent'
        child = 'child'
    structure = models.CharField(max_length=12, choices=ProductStructre.choices, default=ProductStructre.standalone)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='parents')
    product_name = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField(allow_unicode=True, max_length=150)
    upc = models.CharField(max_length=24, unique=True, blank=True, null=True)
    is_publish = models.BooleanField(default=False)
    category = models.ForeignKey('Category.Category', on_delete=models.PROTECT, related_name='product_categories')
    brand = models.ForeignKey('Category.BrandModel', on_delete=models.PROTECT, related_name='product_brand')

    def __str__(self) -> str:
        return self.product_name

    class Meta:
        db_table = 'product'


class ProductImage(CreateModel, UpdateModel):
    image = models.ManyToManyField('images.Image', related_name="product_image_images")
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='product_image_products')
    
    class Meta:
        db_table = 'product_images'


class Attribute(CreateModel, UpdateModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'attribute'


class AttributeValue(CreateModel, UpdateModel):
    attribute_value = models.CharField(max_length=50)
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, related_name='attributes')

    def __str__(self) -> str:
        return f'{self.attribute.name} -- {self.attribute_value}'
    
    class Meta:
        db_table = 'attribute_value'


# through tabel
class ProductLineAttributeValue(CreateModel, UpdateModel):
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.PROTECT, related_name='attribute_value_th')
    product_line = models.ForeignKey(ProductLine, on_delete=models.PROTECT, related_name='product_line_th')
    
    def __str__(self) -> str:
        return self.attribute_value.attribute_value
    
    class Meta:
        db_table = 'attribute_value_through'
        unique_together = ('product_line', 'attribute_value')


class ProductType(CreateModel, UpdateModel):
    class TypeChoose(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        dateetime = 'datetime'
        date = 'date'
        charfield = 'charfield'
        option = 'option'
        multi_option = 'multi_option'
    attribute_title = models.CharField(max_length=50)
    types = models.CharField(max_length=12, choices=TypeChoose.choices, default=TypeChoose.text)
    attribute = models.ManyToManyField(Attribute, related_name='product_type_attribute')
    is_publish = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.attribute_title

    class Meta:
        db_table = 'product_attribute'


class ProductTypeAttrbute(CreateModel, UpdateModel):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f'{self.product_type.attribute_title} -- {self.attribute.name}'
    
    class Meta:
        db_table = 'product_type_attribute_throught'
        unique_together = ('product_type', 'attribute')
        
# class ProductTypeAttribute(CreateModel, UpdateModel):
#     product = models.ForeignKey(ProductModel, on_delete=models.PROTECT, related_name='products')
#     product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='product_types')
#     value_text = models.TextField(blank=True, null=True)
#     value_char = models.CharField(max_length=60)
#     value_integer = models.IntegerField(blank=True, null=True)
#     value_float = models.FloatField(blank=True, null=True)
#     value_datetime = models.DateTimeField(blank=True, null=True)
#     value_date = models.DateField(blank=True, null=True)
#     is_publish = models.BooleanField(default=True)

#     def __str__(self) -> str:
#         return self.product.product_name
    
#     class Meta:
#         db_table = 'product_attribute_value'
