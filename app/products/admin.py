from django.contrib import admin
from .models import Product, ProductLine, ProductType, ProductTypeAttrbute \
    ,ProductLineAttributeValue, Attribute, AttributeValue, ProductImage
from django_jalali.admin.filters import JDateFieldListFilter


class ProductLineInline(admin.TabularInline):
    model = ProductLine
    extra = 0


class AttributeValueInline(admin.TabularInline):
    model = ProductLineAttributeValue
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductLineInline, ProductImageInline)
    raw_id_fields = ('parent', 'category', 'brand', )
    prepopulated_fields = {'slug': ('product_name',)}
    list_editable =('is_publish',)
    list_display = ('product_name','is_publish', 'category', 'brand')
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_per_page = 20    


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = (AttributeValueInline,)
    list_display = ('price', 'is_publish', 'stock_quantity')
    list_editable = ('is_publish',)
    raw_id_fields =('product',)
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_per_page = 20


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('attribute_title', 'types', 'is_publish', 'created_at', 'updated_at')
    list_editable = ('is_publish',)
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_per_page = 20

@admin.register(ProductLineAttributeValue)
class ProductLineAttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductTypeAttrbute)
class ProductTypeAttrbuteAdmin(admin.ModelAdmin):
    pass


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass