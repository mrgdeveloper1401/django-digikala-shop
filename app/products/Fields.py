from django.db import models
from django.core import checks

class OrderFields(models.PositiveSmallIntegerField):
    description = 'Order Fields on unique fields'

    def __init__(self, unique_for_fields=None, *args, **kwargs):
        self.unique_for_fields = unique_for_fields
        return super().__init__(*args, **kwargs)
    
    def check(self, *args, **kwargs):
        return [
            *super().check(*args, **kwargs),
            *self._check_for_fields_attribute(**kwargs)
        ]
    
    def _check_for_fields_attribute(self, **kwargs):
        if self.unique_for_fields is None:
            return [
                checks.Error("OrderFields must defind a unique")
            ]
        elif self.unique_for_fields not in [f.name for f in self._meta.get_fields()]:
            return [
                checks.Error("OrderFields entered does not match en existing fields")
            ]