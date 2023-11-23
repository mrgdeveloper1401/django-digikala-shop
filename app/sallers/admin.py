from django.contrib import admin
from .models import GenuinSaller, legalSaller, MultipleChooseAttribute, Multiplehoose, SignatoryModel \
    , LocationModel


class SignatureInline(admin.TabularInline):
    model = SignatoryModel
    extra = 1

@admin.register(GenuinSaller)
class GenuinSallerAdmin(admin.ModelAdmin):
    ...


@admin.register(legalSaller)
class legalSallerAdmin(admin.ModelAdmin):
    inlines = (SignatureInline,)


@admin.register(MultipleChooseAttribute)
class MultipleChooseAttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(Multiplehoose)
class MultiplehooseAdmin(admin.ModelAdmin):
    pass


@admin.register(SignatoryModel)
class SignatoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(LocationModel)
class LocationAdmin(admin.ModelAdmin):
    pass
