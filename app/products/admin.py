from django.contrib import admin
from . import models

@admin.register(models.ProductModel)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SallerModel)
class SallerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    pass