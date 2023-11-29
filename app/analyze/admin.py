from django.contrib import admin
from .models import ActionHistory


@admin.register(ActionHistory)
class ActionHistoryAdmin(admin.ModelAdmin):
    list_per_page = 20