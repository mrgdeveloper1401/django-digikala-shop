# Generated by Django 4.2.7 on 2023-11-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_imagesmodel_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
