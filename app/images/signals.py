from django.dispatch import receiver
from django.db.models.signals import pre_save
from .exception import DuplicatedImageException
from .models import Image


@receiver(pre_save, sender=Image)
def check_duplicated_image(sender, instance, *args, **kwargs):
    exists = Image.objects.filter(file_hash=instance.file_hash).exists()
    if exists:
        raise DuplicatedImageException('Duplicated image')