import hashlib
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel


class ImagesModel(CreateModel, UpdateModel):
    image = models.ImageField(_('عکس'), upload_to='images/%Y/%m/%d/', height_field='height_image',
                              width_field='width_image')
    display_order = models.PositiveIntegerField(default=0)

    alter_image = models.CharField(_('توضیح در مورد عکس'), max_length=50, null=True, blank=True)
    width_image = models.SmallIntegerField(('عرض') ,editable=False)
    height_image = models.SmallIntegerField(('ارتفاع'), editable=False)

    file_hash = models.CharField(max_length=40, db_index=True, blank=True)
    file_size = models.PositiveIntegerField(null=True, blank=True)

    focal_point_x = models.PositiveIntegerField(null=True, blank=True)
    focal_point_y = models.PositiveIntegerField(null=True, blank=True)
    focal_point_width = models.PositiveIntegerField(null=True, blank=True)
    focal_point_height = models.PositiveIntegerField(null=True, blank=True)
    product_image = models.ForeignKey('products.ProductLineModel', on_delete=models.PROTECT, related_name='images')
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.file_size = self.image.size
        hasher = hashlib.sha1()
        for chunk in self.image.chunks():
            hasher.update(chunk)
        self.file_hash = hasher.hexdigest()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.file_hash} -- {self.product_image}'

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        db_table = 'images'
