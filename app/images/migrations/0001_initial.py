# Generated by Django 4.2.7 on 2023-11-18 08:57

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('alter_image', models.CharField(max_length=50, verbose_name='توضیح در مورد عکس')),
                ('width_image', models.SmallIntegerField(verbose_name='عرض')),
                ('height_image', models.SmallIntegerField(verbose_name='ارتفاع')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'images',
            },
        ),
    ]
