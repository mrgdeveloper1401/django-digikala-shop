# from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from . import models
from django_jalali.admin.filters import JDateFieldListFilter


class ProductOptionInline(admin.TabularInline):
    model = models.ProductAttribute
    extra = 1


@admin.register(models.ProductClass)
class productAdmin(admin.ModelAdmin):
#     list_display = ('title', 'track_stock', 'require_shipping', 'option_product', 'number_of_attribute')
#     search_fields = ('title', )
#     list_filter = (
#         'track_stock',
#         'require_shipping',
#     )
    inlines = (ProductOptionInline, )
#     prepopulated_fields = {'slug': ('title',)}
#     actions = ('disable_track_stock',
#                 'enable_track_stock',
#                 'enable_require_shipping',
#                 'disable_require_shipping')
    
#     def option_product(self, obj):
#         return ','.join([name.title for name in obj.option.all()])
    
#     def number_of_attribute(self, obj):
#         return obj.product_attr.count()
    
#     def disable_track_stock(self, request, queryset):
#         queryset.update(track_stock=False)
        
#     def enable_track_stock(self, request, queryset):
#         queryset.update(track_stock=True)
        
#     def enable_require_shipping(self, request, queryset):
#         queryset.update(require_shipping=True)
        
#     def disable_require_shipping(self, request, queryset):
#         queryset.update(require_shipping=False)
    

admin.site.register(models.OptionGroup)
admin.site.register(models.OptionGroupValue)
admin.site.register(models.ProductAttribute)
admin.site.register(models.Option)