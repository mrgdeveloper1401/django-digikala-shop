# Generated by Django 4.2.7 on 2023-11-18 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('body_question', models.TextField(max_length=500, verbose_name='متن سوال')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_questions', to='products.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('title_comment', models.CharField(max_length=50, verbose_name='عنوان نظر')),
                ('text_comment', models.TextField(max_length=500, verbose_name='نظر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_comments', to='products.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرها',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='AnswerProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('answer_body', models.TextField(max_length=500, verbose_name='متن پاسخ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_answers', to='products.productmodel')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_answers', to='products.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
