# Generated by Django 4.2.7 on 2023-11-30 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0006_alter_category_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandmodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='brandmodel',
            name='updated_at',
        ),
    ]
