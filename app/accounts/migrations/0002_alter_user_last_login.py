# Generated by Django 4.2.7 on 2023-11-30 08:06

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
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2023, 11, 30, 8, 6, 11, 605213, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]