from django.contrib import admin
from .models import GenuinSaller, legalSaller, MultipleChooseAttribute, Multiplehoose, SignatoryModel \
    , LocationModel
from django_jalali.admin.filters import JDateFieldListFilter

class SignatureInline(admin.TabularInline):
    model = SignatoryModel
    extra = 1

@admin.register(GenuinSaller)
class GenuinSallerAdmin(admin.ModelAdmin):
    list_display = ('nation_code', 'shop_name', 'created_at', 'updated_at')
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    search_fields = ('shop_name', 'nation_code', 'created_at', 'updated_at')
    list_per_page = 10


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
