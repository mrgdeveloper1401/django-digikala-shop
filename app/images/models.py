from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel


class ImagesModel(CreateModel, UpdateModel):
    image = models.ImageField(_('عکس'), upload_to='images/%Y/%m/%d/')
    display_order = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        db_table = 'images'
