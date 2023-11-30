from django.db import models
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node
from .managers import CategoryQueryset
from common.models import UpdateModel, CreateModel


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    is_public = models.BooleanField(default=True)
    objects = CategoryQueryset.as_manager()
    
    def __str__(self) -> str:
        return self.title

    
    class Meta:
        db_table = 'category'


class BrandModel(CreateModel, UpdateModel):
    brand_name = models.CharField(max_length=50, db_index=True, unique=True)
    is_publish = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.brand_name
    
    class Meta:
        db_table = 'brand'