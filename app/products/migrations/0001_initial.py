# Generated by Django 4.2.7 on 2023-11-25 06:58

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sallers', '0001_initial'),
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttributeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr', models.CharField(db_index=True, max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
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
                ('attr_value', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'product attribute value',
                'verbose_name_plural': 'product attribute values',
                'db_table': 'product_attribute_value',
            },
        ),
        migrations.CreateModel(
            name='ProductLineAttributeValueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ بروزرسانی')),
                ('attr_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_attr_values', to='products.productattributevaluemodel')),
                ('attribute_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productattributemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ بروزرسانی')),
                ('product_name', models.CharField(db_index=True, max_length=150, verbose_name='نام کالا')),
                ('slug', models.SlugField(allow_unicode=True, max_length=150, unique=True)),
                ('description_product', models.TextField(blank=True, null=True, verbose_name='معرفی کالا')),
                ('is_active', models.BooleanField(default=True)),
                ('warrenty_choose', models.CharField(choices=[('no warrenty', 'no warrenty'), ('company warrenty', 'company warrenty')], default='no warrenty', max_length=16, verbose_name='نوع گارانتی')),
                ('company_warrent_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام شرکت گارانتی کننده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='Category.category')),
                ('saller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sallers', to='sallers.genuinsaller')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductLineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='تاریخ بروزرسانی')),
                ('upc', models.CharField(max_length=20, unique=True, verbose_name='بارکد')),
                ('sku', models.CharField(max_length=50, unique=True, verbose_name='بارکد اختصاصی انبارداری')),
                ('price', models.DecimalField(decimal_places=3, max_digits=12, verbose_name='قیمت کالا')),
                ('is_stock', models.BooleanField(default=True, verbose_name='موجود هست')),
                ('is_delivery', models.BooleanField(default=True, verbose_name='ارسال از طریق پست')),
                ('number_product', models.PositiveSmallIntegerField(verbose_name='تعداد محصول')),
                ('is_active', models.BooleanField(default=True)),
                ('attribute_value', models.ManyToManyField(through='products.ProductLineAttributeValueModel', to='products.productattributemodel')),
                ('product_line', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_lines', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'product line',
                'verbose_name_plural': 'product lines',
                'db_table': 'product_line',
            },
        ),
        migrations.AddField(
            model_name='productlineattributevaluemodel',
            name='product_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_line_attr_values', to='products.productlinemodel'),
        ),
        migrations.AlterUniqueTogether(
            name='productlineattributevaluemodel',
            unique_together={('attr_value', 'product_line')},
        ),
    ]