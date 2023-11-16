# Generated by Django 4.2.7 on 2023-11-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesmodel',
            name='alter_image',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='توضیح در مورد عکس'),
        ),
        migrations.AddField(
            model_name='imagesmodel',
            name='height_image',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='ارتفاع'),
        ),
        migrations.AddField(
            model_name='imagesmodel',
            name='width_image',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='عرض'),
        ),
    ]
