from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    pass
