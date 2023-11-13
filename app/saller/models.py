from django.db import models
from common.models import CreateModel, UpdateModel
from django.utils.translation import gettext_lazy as _


class SallerModel(CreateModel):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='users')
    product_name = models.CharField(_('نام کالا'), max_length=150, db_index=True)
    price = models.PositiveIntegerField(_('قیمت'), db_index=True)
    
    class Warrentychoose(models.TextChoices):
        np_warrenty = 'no warrenty', _('no warrenty')
        company_warrenty = 'company warrenty', _('company warrenty')
        
    warrenty_choose = models.CharField(_('نوع گارانتی'), max_length=16, default=Warrentychoose.choices, choices=Warrentychoose.company_warrenty)
    is_stock = models.BooleanField(_("موجود هست"), default=True)
    number_product = models.PositiveSmallIntegerField(_("تعداد محصول"))
    # image = models.ForeignKey()
    
    
    
# class WarrentyModel(CreateModel, UpdateModel):
    
