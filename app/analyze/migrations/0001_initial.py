# Generated by Django 4.2.7 on 2023-12-03 03:52

import django.contrib.admin.models
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
            ],
            options={
                'db_table': 'action_history',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('admin.logentry',),
            managers=[
                ('objects', django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]
