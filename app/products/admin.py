from django.contrib import admin
from . import models


class ProductLineInline(admin.TabularInline):
    model = models.ProductLine
    extra = 0

class SallerInline(admin.TabularInline):
    model = models.SallerModel
    extra = 0

@admin.register(models.ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductLineInline, SallerInline)


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SallerModel)
class SallerAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProductAttributeModel)
class ProductAttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductAttributeValueModel)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass

