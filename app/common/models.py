from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from django.utils import timezone
from django.db.models import QuerySet, Manager, Q


class SoftQueryset(QuerySet):
    def delete(self):
        return self.update(is_deleted=True, deleted_at=timezone.now(), is_active=False)


class SoftManager(Manager):
    def get_queryset(self):
        return super().get_queryset(self.model, self._db).filter(Q(is_deleted=True) | Q(is_deleted__isnull=True))


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False, null=True, blank=True, editable=False)
    deleted_at  = jmodels.jDateTimeField(null=True, blank=True, editable=False)
    objects = SoftManager()

    class Meta:
        abstract = True
    
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]:
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.is_active = False
        self.save()

# create model
class CreateModel(models.Model):
    created_at = jmodels.jDateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class UpdateModel(models.Model):
    updated_at = jmodels.jDateTimeField(auto_now=True, editable=False, blank=True, null=True)

    class Meta:
        abstract = True
