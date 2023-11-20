from django.dispatch import receiver
from django.db.models.signals import pre_save
from .exception import DuplicatedImageException
from .models import ImagesModel


@receiver(pre_save, sender=ImagesModel)
def check_duplicated_image(sender, instance, *args, **kwargs):
    exists = ImagesModel.objects.filter(file_hash=instance.file_hash).exists()
    if exists:
        raise DuplicatedImageException('Duplicated image')