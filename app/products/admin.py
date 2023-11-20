from django.contrib import admin
from . import models


class ProductAttributeInline(admin.TabularInline):
    model = models.ProductAttributeModel
    extra = 0


class ProductLineInline(admin.TabularInline):
    model = models.ProductLine
    extra = 0


class ProductAttributeValueInline(admin.TabularInline):
    model = models.ProductAttributeValueModel
    extra = 0


@admin.register(models.ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductLineInline, ProductAttributeInline, ProductAttributeValueInline)
    raw_id_fields = ('category', 'saller')
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('category', 'product_name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('product_name',)
    list_filter = ('is_active', 'created_at', 'updated_at')
    list_editable = ('is_active',)
    list_per_page = 20
    filter_horizontal = ('options',)


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SallerModel)
class SallerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('company_name',)}

    fieldsets = (
        ('کاربر', {'fields': ('user',)}),
        ('مشخصات فروشنده', {'fields': ('company_name', 'slug', 'province_name', 'eprachy_name', 'city', 'address', 'postacl_code')})
    )
    list_display = ('user', 'company_name', 'created_at', 'id')
    search_fields = ('company_name',)
    list_filter = ('created_at', )
    list_per_page = 20


@admin.register(models.ProductAttributeModel)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')
    list_per_page = 20


@admin.register(models.ProductAttributeValueModel)
class ProductAttributeValueModel(admin.ModelAdmin):
    list_display = ('title', 'product')
    list_per_page = 20