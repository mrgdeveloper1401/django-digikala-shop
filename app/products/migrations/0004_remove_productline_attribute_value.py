# Generated by Django 4.2.7 on 2023-12-03 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_attributevalue_product_line'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productline',
            name='attribute_value',
        ),
    ]
