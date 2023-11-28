from django.db import models
from django.utils.translation import gettext_lazy as _
from treebeard.mp_tree import MP_Node
from .managers import CategoryQueryset
from django.utils.text import slugify


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    is_public = models.BooleanField(default=True)

    objects = CategoryQueryset.as_manager()
    
    def __str__(self) -> str:
        return self.title

    
    class Meta:
        db_table = 'category'
