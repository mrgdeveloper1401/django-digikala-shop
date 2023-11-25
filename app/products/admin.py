from django.contrib import admin
from .models import ProductAttributeModel, ProductAttributeValueModel \
, ProductModel, ProductLineModel
from images.models import ImagesModel


class ImageInline(admin.TabularInline):
    model = ImagesModel
    extra = 0


# class ProductAttributeInline(admin.TabularInline):
#     model = ProductAttributeModel
#     extra = 0



# class ProductAttributeValueInline(admin.TabularInline):
#     model = ProductAttributeValueModel
#     extra = 0


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    raw_id_fields = ('category',)
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('category', 'product_name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('product_name',)
    list_filter = ('is_active', 'created_at', 'updated_at')
    list_editable = ('is_active',)
    list_per_page = 20


@admin.register(ProductAttributeModel)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('attr', 'description')
    list_per_page = 20


@admin.register(ProductAttributeValueModel)
class ProductAttributeValueModel(admin.ModelAdmin):
    list_display = ('attr_value', )
    list_per_page = 20


@admin.register(ProductLineModel)
class ProductLineAdmin(admin.ModelAdmin):
    # list_display = ('upc','sku', 'price', 'is_stock', 'is_delivery', 'number_product', 'is_active', 'product_line')
    list_per_page = 20