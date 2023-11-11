from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels


class OptionGroup(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Option Group"
        verbose_name_plural = "Option Groups"


class OptionGroupValue(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE,
                              related_name='groups')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Option Group Value"
        verbose_name_plural = "Option Group Values"
        
        
class ProductModel(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(_('معرفی کالا'), max_length=2048, null=True, blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    track_stock = models.BooleanField(default=True)
    require_shipping = models.BooleanField(default=True)
    option = models.ManyToManyField(
        OptionGroup,
        blank=True,
        related_name='product_options',
    )


    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "product class"
        verbose_name_plural = "product classes"


class ProductAttribute(models.Model):
    product_parent = models.ForeignKey(
        'ProductModel',
        on_delete=models.CASCADE,
        related_name='product_attr',
    )
    attr_title = models.CharField(
        _('عنوان ويژگی'),
        max_length=50
    )
    attr_text = models.CharField(
        _('متن ویژگی'),
        max_length=50
    )
    
    def __str__(self) -> str:
        return self.product_parent.title
    
    
class Option(models.Model):
    class OptionTypeChoice(models.TextChoices):
        text = 'text'
        integer = 'integer'
        float = 'float'
        option = 'option'
        multi_option = 'multi_option'

    title = models.CharField(max_length=64)
    type = models.CharField(max_length=16, choices=OptionTypeChoice.choices, default=OptionTypeChoice.text)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null=True, blank=True,
                                     related_name='option_groups')
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.title
