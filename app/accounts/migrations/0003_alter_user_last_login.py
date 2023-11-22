# Generated by Django 4.2.7 on 2023-11-22 07:46

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2023, 11, 22, 7, 46, 12, 934706, tzinfo=datetime.timezone.utc), null=True, verbose_name='تاریخ اخرین ورود'),
        ),
    ]