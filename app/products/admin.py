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


@admin.register(ProductAttributeValueModel)
class ProductLineAttributeValueAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    ...
    # raw_id_fields = ('category', 'saller', 'brand')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = (ProductAttributeValueInline,)
    list_display = ('category', 'product_name', 'is_public', 'created_at', 'updated_at')
    search_fields = ('product_name',)
    list_filter = ('is_public', ('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_editable = ('is_public',)
    list_per_page = 20


@admin.register(OptionGroup)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_per_page = 20


# @admin.register(OptionGroupValue)
# class ProductAttributeValueModel(admin.ModelAdmin):
#     list_display = ('title', 'option_group', 'creatdate', 'updated_at')
#     search_fields = ('title',)
#     list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
#     list_per_page = 20


@admin.register(ProductLineModel)
class ProductLineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title_productLine',)}
    list_display = ('title_productLine', 'created_at', 'updated_at', 'is_publish', 'has_attribute', 'attribute_count')
    inlines = (ProductAttributeInline,)
    list_per_page = 20
    list_editable = ('is_publish',)
    search_fields = ('title_productLine', )
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))


@admin.register(ProductAttributeModel)
class ProductTypeAttributeAdmin(admin.ModelAdmin):
    list_display = ('attribute_title', 'types', 'option_group', 'product_line', 'is_active', 'created_at', 'updated_at')
    search_fields = ('attribute_title', 'product_line')
    list_filter = ('is_active', ('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_editable = ('is_active',)