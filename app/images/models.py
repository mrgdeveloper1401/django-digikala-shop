import hashlib
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CreateModel, UpdateModel


class ImagesModel(CreateModel, UpdateModel):
    image = models.ImageField(upload_to='images/%Y/%m/%d/', height_field='height_image',
                              width_field='width_image')
    display_order = models.PositiveIntegerField(default=0)

    alter_image = models.CharField(max_length=50, null=True, blank=True)
    width_image = models.SmallIntegerField(editable=False)
    height_image = models.SmallIntegerField(editable=False)

    file_hash = models.CharField(max_length=40, db_index=True, blank=True)
    file_size = models.PositiveIntegerField(null=True, blank=True)

    focal_point_x = models.PositiveIntegerField(null=True, blank=True)
    focal_point_y = models.PositiveIntegerField(null=True, blank=True)
    focal_point_width = models.PositiveIntegerField(null=True, blank=True)
    focal_point_height = models.PositiveIntegerField(null=True, blank=True)
    is_publish = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.file_size = self.image.size
        hasher = hashlib.sha1()
        for chunk in self.image.chunks():
            hasher.update(chunk)
        self.file_hash = hasher.hexdigest()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.file_hash}'

    class Meta:
        db_table = 'images'
