from django.contrib import admin
from .models import GenuinSaller, legalSaller, MultipleChooseAttribute, Multiplehoose, SignatoryModel


@admin.register(GenuinSaller)
class GenuinSallerAdmin(admin.ModelAdmin):
    pass


@admin.register(legalSaller)
class legalSallerAdmin(admin.ModelAdmin):
    pass


@admin.register(MultipleChooseAttribute)
class MultipleChooseAttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(Multiplehoose)
class MultiplehooseAdmin(admin.ModelAdmin):
    pass


@admin.register(SignatoryModel)
class SignatoryModelAdmin(admin.ModelAdmin):
    pass