from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Category, BrandModel
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(Category)
class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    prepopulated_fields = {
        'slug': ('title', )
    }
    list_display = ('title', 'id')
    search_fields = ('title', )


@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'is_publish', )
    search_fields = ('brand_name',)
    list_filter = ('is_publish', 'brand_name', ('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    list_per_page = 20