# Generated by Django 4.2.7 on 2023-11-27 22:15

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userproxy_alter_jobusermodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recycleuser',
            options={},
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2023, 11, 27, 22, 15, 41, 45009, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
