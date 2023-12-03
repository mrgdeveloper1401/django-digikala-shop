from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel


# product line model
class ProductLine(CreateModel, UpdateModel):
    price = models.DecimalField(decimal_places=3, max_digits=12)
    sku = models.CharField(max_length=24, unique=True, blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_publish = models.BooleanField(default=True)
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
    description = models.TextField(blank=True, null=True)
    upc = models.CharField(max_length=24, unique=True, blank=True, null=True)
    is_publish = models.BooleanField(default=False)
    category = models.ForeignKey('Category.Category', on_delete=models.PROTECT, related_name='product_categories')
    brand = models.ForeignKey('Category.BrandModel', on_delete=models.PROTECT, related_name='product_brand')
    
    
    @property
    def has_attribute_products(self):
        return self.attribute_products.exists()
    
    @property
    def attribute_count(self):
        return self.attribute_products.count()
    
    def __str__(self) -> str:
        return self.product_name

    class Meta:
        db_table = 'product'


class ProductImage(CreateModel, UpdateModel):
    image = models.ForeignKey('images.Image', on_delete=models.PROTECT, related_name="product_image_images")
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='product_image_products')
    
    class Meta:
        db_table = 'product_images'


class Attribute(CreateModel, UpdateModel):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='attribute_products')
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        db_table = 'attribute'


class AttributeValue(CreateModel, UpdateModel):
    attribute_value = models.CharField(max_length=50)
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, related_name='attributes')
    product_line = models.ForeignKey(ProductLine, on_delete=models.PROTECT, related_name='attribute_value_product_line')
    product_type = models.ForeignKey('ProductType', on_delete=models.PROTECT, related_name='product_types', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.attribute.name} -- {self.attribute_value}'
    
    class Meta:
        db_table = 'attribute_value'


class ProductType(CreateModel, UpdateModel):
    class TypeChoose(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        datetime = 'datetime'
        date = 'date'
        charfield = 'charfield'
    types = models.CharField(max_length=12, choices=TypeChoose.choices, default=TypeChoose.text, unique=True)
    is_publish = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.types

    class Meta:
        db_table = 'product_attribute'
