from django.contrib import admin
from .models import ImagesModel


@admin.register(ImagesModel)
class ImagesAdmin(admin.ModelAdmin):
    pass
