from django.contrib import admin
from .models import Product, ProductLine, ProductType, ProductTypeAttrbute \
    ,ProductLineAttributeValue
from django_jalali.admin.filters import JDateFieldListFilter


class ProductLineInline(admin.TabularInline):
    model = ProductLine
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductLineInline,)
    raw_id_fields = ('parent', 'category', 'brand', )
    prepopulated_fields = {'slug': ('product_name',)}
    filter_horizontal = ('image',)
    list_editable =('is_publish',)
    list_display = ('product_name','is_publish', 'category', 'brand')
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_per_page = 20    


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
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
