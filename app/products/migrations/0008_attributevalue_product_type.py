# Generated by Django 4.2.7 on 2023-12-03 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_producttype_produt_type_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributevalue',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_types', to='products.producttype'),
        ),
    ]