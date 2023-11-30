from django.contrib import admin
from .models import OptionGroup, ProductAttributeModel, ProductAttributeValueModel, ProductLineModel \
    ,ProductModel
from django_jalali.admin.filters import JDateFieldListFilter


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttributeModel
    extra = 1


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValueModel
    extra = 1


class ProducLineInline(admin.TabularInline):
    model = ProductLineModel
    extra = 1


@admin.register(ProductAttributeValueModel)
class ProductLineAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_attribute', 'value_text', 'value_integer', 'value_float', 'value_datetime', 'value_date', 'is_publish', )
    list_editable = ('is_publish',)
    search_fields = ('product', 'product_attribte', 'value_text', 'value_integer', 'value_float', 'value_datetime', 'value_date')
    list_per_page = 20
    raw_id_fields = ('product', 'product_attribute')


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    ...
    raw_id_fields = ('parent', 'category', 'brand',)
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = (ProductAttributeValueInline, ProducLineInline)
    list_display = ('category', 'product_name', 'is_publish', 'created_at', 'updated_at')
    search_fields = ('product_name',)
    list_filter = ('is_publish', ('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_editable = ('is_publish',)
    list_per_page = 20


@admin.register(OptionGroup)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_publish', 'updated_at')
    search_fields = ('title',)
    list_editable = ('is_publish',)
    list_filter = ('is_publish', ('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_per_page = 20


@admin.register(ProductLineModel)
class ProductLineAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'sku', 'stock_quantity', 'is_publish', 'has_attribute', 'attribute_count')
    inlines = (ProductAttributeInline,)
    list_per_page = 20
    list_editable = ('is_publish',)
    list_filter = ('is_publish', ('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))


@admin.register(ProductAttributeModel)
class ProductTypeAttributeAdmin(admin.ModelAdmin):
    list_display = ('attribute_title', 'types', 'option_group', 'product_line', 'is_publish', 'created_at', 'updated_at')
    search_fields = ('attribute_title', 'product_line')
    list_filter = ('is_publish', ('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_editable = ('is_publish',)
    