# Generated by Django 4.2.7 on 2023-12-03 08:19

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2023, 12, 3, 8, 19, 10, 911737, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]