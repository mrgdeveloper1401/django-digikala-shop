from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel


class ImagesModel(CreateModel, UpdateModel):
    image = models.ImageField(_('عکس'), upload_to='images/%Y/%m/%d/')
    display_order = models.PositiveIntegerField(default=0)
<<<<<<< HEAD
    alter_image = models.CharField(_('توضیح در مورد عکس'), max_length=50)
    width_image = models.SmallIntegerField(('عرض'))
    height_image = models.SmallIntegerField(('ارتفاع'))
=======
    alter_image = models.CharField(_('توضیح در مورد عکس'), max_length=50, blank=True, null=True)
    width_image = models.SmallIntegerField(('عرض'), blank=True, null=True)
    height_image = models.SmallIntegerField(('ارتفاع'), blank=True, null=True)
>>>>>>> 55ba428b8a1393461da1696098f1ac5b03e8cf97
    
    
    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        db_table = 'images'
