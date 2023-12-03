# Generated by Django 4.2.7 on 2023-12-03 00:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', django_jalali.db.models.jDateTimeField(blank=True, editable=False, null=True)),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile_phone', models.CharField(max_length=11, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_day', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified_email', models.BooleanField(default=False)),
                ('is_verified_mmobile_phone', models.BooleanField(default=False)),
                ('last_login', django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2023, 12, 3, 0, 42, 18, 991663, tzinfo=datetime.timezone.utc), null=True)),
                ('nation_code', models.CharField(blank=True, help_text='max length 10 characters', max_length=10, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=6)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='LegalUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('organization_name', models.CharField(max_length=100)),
                ('economy_code', models.CharField(help_text='max length 12 characters', max_length=12, unique=True)),
                ('nation_code_organization', models.CharField(help_text='max length 11 characters', max_length=11, unique=True)),
                ('state_name', models.CharField(blank=True, max_length=50, null=True)),
                ('city_name', models.CharField(blank=True, max_length=10, null=True)),
                ('landing_phone', models.CharField(max_length=11)),
                ('is_enable', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'legal_user',
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='JobUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('job', models.CharField(choices=[('IT', 'It'), ('financial accounting', 'Financial Accounting'), ('sale marketing', 'Sale Marketing'), ('health medical', 'Health Medicine'), ('education training', 'Education Training'), ('engineer construction', 'Engineer Constraction'), ('art design', 'Art Design'), ('restaurant food services', 'Restaurent Food Services'), ('commercial legal', 'Commercial Legal'), ('environment sustainability', 'Environment Sustainablity')], default=None, max_length=26)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='RecycleUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('deleted', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='RecycleLegalUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.legaluser',),
            managers=[
                ('deleted', django.db.models.manager.Manager()),
            ],
        ),
    ]
