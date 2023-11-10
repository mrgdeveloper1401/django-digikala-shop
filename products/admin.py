from typing import Any
from django.contrib import admin
from .models import ProductModel, 
from django_jalali.admin.filters import JDateFieldListFilter



@admin.register(ProductModel)
class productAdmin(admin.ModelAdmin):
    list_display = ('en_name', 'fa_name', 'price', 'is_public', 'id')
    list_filter = (
        ('create_product', JDateFieldListFilter),
        ('update_product', JDateFieldListFilter),
        'is_public',
        'is_available',
        'in_stock',
    )
    list_editable = ('is_public', )
    list_per_page = 100
    # inlines = (ProductColorModel,)
    date_hierarchy = 'create_product'
    prepopulated_fields = {
        'slug': ('description',)
    }
    search_fields = ('en_name', )
    readonly_fields = ('create_product', 'update_product')
    show_full_result_count = True
    ordering = ('-create_product',)
    
    def tick_is_publicc(self, obj):
        return obj.is_public.bool
    