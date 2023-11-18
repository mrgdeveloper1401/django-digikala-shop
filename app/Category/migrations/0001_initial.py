# Generated by Django 4.2.7 on 2023-11-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('is_public', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'db_table': 'category',
            },
        ),
    ]
