from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.geos import Point
from .models import LocationModel

@receiver(post_save, sender=LocationModel)
def handle_location_change(sender, instance, **kwargs):
    if kwargs.get('created', False) or 'location' in kwargs.get('update_fields', []):
        pass
