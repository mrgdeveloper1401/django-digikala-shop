# Generated by Django 4.2.7 on 2023-11-30 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_productlinemodel_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='product_line',
        ),
        migrations.AlterField(
            model_name='productlinemodel',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='line_products', to='products.productmodel'),
        ),
    ]
