# Generated by Django 4.2.7 on 2023-11-23 10:19

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
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ بروزرسانی')),
                ('image', models.ImageField(height_field='height_image', upload_to='images/%Y/%m/%d/', verbose_name='عکس', width_field='width_image')),
                ('display_order', models.PositiveIntegerField(default=0)),
                ('alter_image', models.CharField(blank=True, max_length=50, null=True, verbose_name='توضیح در مورد عکس')),
                ('width_image', models.SmallIntegerField(editable=False, verbose_name='عرض')),
                ('height_image', models.SmallIntegerField(editable=False, verbose_name='ارتفاع')),
                ('file_hash', models.CharField(blank=True, db_index=True, max_length=40)),
                ('file_size', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'images',
            },
        ),
    ]
