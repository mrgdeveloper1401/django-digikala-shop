from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel


class ImagesModel(CreateModel, UpdateModel):
    image = models.ImageField(_('عکس'), upload_to='images/%Y/%m/%d/')
    # choose_image = models.ManyToManyField('self')
    display_order = models.PositiveIntegerField(default=0)

    alter_image = models.CharField(_('توضیح در مورد عکس'), max_length=50)
    width_image = models.SmallIntegerField(('عرض'), default=1280)
    height_image = models.SmallIntegerField(('ارتفاع'), default=720)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        db_table = 'images'
