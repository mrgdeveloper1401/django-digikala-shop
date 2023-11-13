# Generated by Django 4.2.7 on 2023-11-13 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ بروزرسانی')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='عکس')),
                ('display_order', models.PositiveIntegerField(default=0)),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'images',
            },
        ),
    ]
