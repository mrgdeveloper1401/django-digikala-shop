from django.db.models import Manager
from django.db.models.query import QuerySet


class PublishProductManager(Manager):
    def is_public(self):
        return self.filter(is_public=True)
    
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_public=True)