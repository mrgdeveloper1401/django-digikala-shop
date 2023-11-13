from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from common.fields import UpperCharField
from common.models import CreateModel, UpdateModel


class Option(CreateModel):
    title = models.CharField(_('عنوان'), max_length=50, db_index=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')
        db_table = 'option'
        

class ProductModel(CreateModel, UpdateModel):
    category = models.ForeignKey('Category.Category', on_delete=models.PROTECT, related_name='categories')
    title_product = models.CharField(_('نام یا عنوان محصول'), max_length=150, db_index=True)
    description_product = models.TextField(blank=True, null=True)
    barcode = models.BigIntegerField(_('بارکد کالا'))
    product_auth_code = models.CharField(_('کد شناسایی هر کالا'), max_length=128, unique=True)
    option = models.ManyToManyField(Option, related_name='options', blank=True, null=True)
    saller = models.ForeignKey('saller.SallerModel', on_delete=models.PROTECT, related_name='sallers')
    