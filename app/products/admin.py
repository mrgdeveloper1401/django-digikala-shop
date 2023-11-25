from django.contrib import admin
from .models import ProductAttributeModel, ProductAttributeValueModel \
, ProductModel, ProductLineModel, ProductLineAttributeValueModel, BrandModel \
    ,ProductTypeAttributeModel, ProductTypeModel
from images.models import ImagesModel
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(ProductLineAttributeValueModel)
class ProductLineAttributeValueAdmin(admin.ModelAdmin):
    pass


class ImageInline(admin.TabularInline):
    model = ImagesModel
    extra = 0


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category', 'saller', 'brand')
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('category', 'product_name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('product_name',)
    list_filter = ('is_active', ('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_editable = ('is_active',)
    list_per_page = 20


@admin.register(ProductAttributeModel)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('attr', 'description')
    list_per_page = 20


@admin.register(ProductAttributeValueModel)
class ProductAttributeValueModel(admin.ModelAdmin):
    list_display = ('attr_value', 'created_at', 'updated_at')
    list_per_page = 20


class ProductLineAttributeValueInline(admin.TabularInline):
    model = ProductLineAttributeValueModel
    extra = 0


@admin.register(ProductLineModel)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = (ProductLineAttributeValueInline, ImageInline)
    raw_id_fields = ('product',)
    list_per_page = 20
    list_display = ('upc', 'sku', 'price', 'is_stock', 'is_delivery', 'is_active', 'number_product',)
    list_editable = ('is_delivery', 'is_active', 'number_product', 'is_stock')
    search_fields = ('price', )
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    

@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'created_at', 'updated_at')
    list_per_page = 20
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    search_fields = ('brand_name',)
    prepopulated_fields = {'slug': ('brand_name',)}
    

@admin.register(ProductTypeModel)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductTypeAttributeModel)
class ProductTypeAttributeAdmin(admin.ModelAdmin):
    pass