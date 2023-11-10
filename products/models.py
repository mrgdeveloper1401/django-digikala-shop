from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels



class ProductModel(models.Model):
    en_name = models.CharField(_('english name'),
                               max_length=100,
                               db_index=True)
    fa_name = models.CharField(_('fa name'),
                               max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True,
                            max_length=100)
    create_product = jmodels.jDateTimeField(_('create product'),
                                            auto_now_add=True)
    update_product = jmodels.jDateTimeField(_('update product'),
                                            auto_now=True)
    price = models.DecimalField(
        decimal_places=3,
        max_digits=12
    )
    is_public = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    in_stock = models.PositiveSmallIntegerField(
        _('موجودی انبار')
    )
    require_shipping = models.BooleanField(_('ارسال از طریق پست'),
                                           default=True)
    def __str__(self) -> str:
        return self.en_name
    
    
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        db_table = 'product'
        
        
class OptionGroup(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('option group')
        verbose_name_plural = _('option groups')
        db_table = 'option_groups'
        
        
class OptionGroupValue(models.Model):
    title = models.CharField(max_length=100)
    group = models.ForeignKey(OptionGroup,
                              on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        verbose_name = _('OptionGroupValue')
        verbose_name_plural = _('OptionGroupValues')
        db_table = 'option_group_values'
        

class ProductAttribute(models.Model):
    
    
    class AttrTypechoose(models.TextChoices):
        
    product_class = models.ForeignKey(ProductModel,
                                      on_delete=models.CASCADE,
                                      null=True)