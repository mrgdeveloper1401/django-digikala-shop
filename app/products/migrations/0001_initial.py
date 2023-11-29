# Generated by Django 4.2.7 on 2023-11-29 18:40

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'option_groups',
            },
        ),
        migrations.CreateModel(
            name='ProductAttributeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('types', models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('float', 'Float'), ('datetime', 'Dateetime'), ('option', 'Option'), ('multi_option', 'Multi Option')], default='text', max_length=12)),
                ('attribute_title', models.CharField(max_length=50)),
                ('option_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='option_groups', to='products.optiongroup')),
            ],
            options={
                'db_table': 'product_attribute',
            },
        ),
        migrations.CreateModel(
            name='ProductLineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('title_productLine', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True)),
                ('description', models.TextField(help_text='explain description product')),
                ('require_shipping', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'product_line',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('structure', models.CharField(choices=[('standalone', 'Standallowne'), ('parent', 'Parent'), ('child', 'Child')], default='standalone', max_length=12)),
                ('product_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True)),
                ('upc', models.CharField(blank=True, max_length=24, null=True, unique=True)),
                ('is_public', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_categories', to='Category.category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parents', to='products.productmodel')),
                ('product_line', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_classes', to='products.productlinemodel')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductAttributeValueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, null=True)),
                ('value_text', models.TextField()),
                ('value_integer', models.IntegerField()),
                ('value_float', models.FloatField()),
                ('value_datetime', models.DateTimeField()),
                ('value_date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.productmodel')),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_attributes', to='products.productattributemodel')),
            ],
            options={
                'db_table': 'product_attribute_value',
            },
        ),
        migrations.AddField(
            model_name='productattributemodel',
            name='product_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_lines', to='products.productlinemodel'),
        ),
    ]
