# Generated by Django 4.2.7 on 2023-11-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_update_at_sallermodel_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='options',
            field=models.ManyToManyField(blank=True, to='products.option'),
        ),
    ]
