# Generated by Django 4.2.7 on 2023-12-03 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import mptt.fields


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
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('body_question', models.TextField(max_length=500)),
                ('is_active', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_questions', to='products.product')),
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
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('rate_choose', models.CharField(choices=[('one', 'One'), ('tow', 'Tow'), ('three', 'Three'), ('four', 'Four'), ('five', 'Five')], default='five', max_length=5)),
                ('title_comment', models.CharField(max_length=50)),
                ('text_comment', models.TextField(max_length=500)),
                ('is_active', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_comments', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='AnswerProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('relation_choose', models.CharField(blank=True, choices=[('like', 'Like'), ('dislike', 'Dislike')], default=None, max_length=7)),
                ('answer_body', models.TextField(max_length=500)),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='question.answerproduct')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_answers', to='products.product')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='question.questionmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
