# Generated by Django 4.2.7 on 2023-11-18 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
        ('Category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'option',
                'verbose_name_plural': 'options',
                'db_table': 'option',
            },
        ),
        migrations.CreateModel(
            name='ProductAttributeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='عنوان ویژگی')),
            ],
            options={
                'verbose_name': 'product attribute',
                'verbose_name_plural': 'product attrobutes',
                'db_table': 'product_attribute',
            },
        ),
        migrations.CreateModel(
            name='ProductAttributeValueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='ویژگی')),
            ],
            options={
                'verbose_name': 'product attribute value',
                'verbose_name_plural': 'product attribute values',
                'db_table': 'product_attribute_value',
            },
        ),
        migrations.CreateModel(
            name='SallerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('update_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ بروزرسانی')),
                ('company_name', models.CharField(max_length=50, verbose_name='اسم تولیدی')),
                ('province_name', models.CharField(max_length=50, verbose_name='استان')),
                ('eprachy_name', models.CharField(max_length=50, verbose_name='شهرستان')),
                ('city', models.CharField(max_length=50, verbose_name='شهر')),
                ('address', models.TextField(verbose_name='ادرس')),
                ('postacl_code', models.CharField(max_length=11, unique=True, verbose_name='کد پستی')),
                ('nation_code', models.CharField(max_length=11, unique=True, verbose_name='کد ملی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'saller',
                'verbose_name_plural': 'sellers',
                'db_table': 'saller',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('product_name', models.CharField(db_index=True, max_length=150, verbose_name='نام کالا')),
                ('price', models.PositiveIntegerField(db_index=True, verbose_name='قیمت')),
                ('description_product', models.TextField(blank=True, null=True)),
                ('barcode', models.PositiveBigIntegerField(blank=True, verbose_name='بارکد کالا')),
                ('product_auth_code', models.CharField(max_length=128, unique=True, verbose_name='کد شناسایی هر کالا')),
                ('is_stock', models.BooleanField(default=True, verbose_name='موجود هست')),
                ('number_product', models.PositiveSmallIntegerField(verbose_name='تعداد محصول')),
                ('is_delivery', models.BooleanField(default=True, verbose_name='ارسال از طریق پست')),
                ('warrenty_choose', models.CharField(choices=[('no warrenty', 'no warrenty'), ('company warrenty', 'company warrenty')], default='no warrenty', max_length=16, verbose_name='نوع گارانتی')),
                ('company_warrent_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام شرکت گارانتی کننده')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='Category.category')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_images', to='images.imagesmodel')),
                ('saller', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='sallers', to='products.sallermodel')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
    ]
