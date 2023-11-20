from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from django_jalali.admin.filters import JDateFieldListFilter
from .models import User, JobUserModel, RecycleUser


@admin.register(User)
class UsersAdmin(UserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "mobile_phone", 'birth_day', 'gender')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    'is_deleted',
                    "groups",
                    "user_permissions",

                ),
            },
        ),
        ('accept account', {'fields': ('is_verified_email', 'is_verified_mmobile_phone',)}),
        (_("Important dates"), {"fields": ("last_login", 'updated_at', 'deleted_at',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", 'mobile_phone', "password1", "password2"),
            },
        ),
    )
    list_display = ("mobile_phone", "email", "first_name", "last_name", 'created_at', 'updated_at')
    list_filter = ("is_staff", "is_superuser", "is_active", ("created_at", JDateFieldListFilter), 
                   ('updated_at', JDateFieldListFilter))
    search_fields = ("mobile_phone", "first_name", "last_name", "email")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    list_display_links = ('mobile_phone', 'email')
    readonly_fields = ('updated_at', 'is_deleted', 'deleted_at',)
    list_per_page = 20
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return User.objects.filter(is_deleted=False)


@admin.register(RecycleUser)
class RecycleAdmin(admin.ModelAdmin):
    actions = ('recover user',)
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return RecycleUser.deleted.filter(is_deleted=True)
    
    @admin.action(description='recovery user')
    def recover(self, request: HttpRequest, queryset: QuerySet[Any]):
        queryset.update(is_deleted=False, deleted_at=None)
        

@admin.register(JobUserModel)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'id')
    search_fields = ('job', )
    list_filter =(('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter))
    raw_id_fields = ('user',)
    list_display_links =('job', 'user')