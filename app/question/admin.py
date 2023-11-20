from django.contrib import admin
from .models import AnswerProduct, CommentProduct, QuestionModel


@admin.register(AnswerProduct)
class AnswerProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'product', 'question')
    list_display = ('user', 'question', 'product', 'answer_body', 'is_active', 'created_at',)
    list_editable = ('is_active', )
    search_fields = ('answer_body',)
    list_filter = ('is_active', 'created_at', 'is_active')
    list_per_page = 20



@admin.register(CommentProduct)
class CommentProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'product', 'title_comment', 'created_at', 'rate_choose',)
    raw_id_fields = ('user', 'product')
    list_per_page = 20
    search_fields = ('rate_choose',)
    list_filter = ('rate_choose', 'created_at', 'is_active')
    list_editable = ('is_active',)

@admin.register(QuestionModel)
class QuestionModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'product')
    list_display = ('user', 'body_question', 'is_active', 'product', 'created_at',)
    list_editable = ('is_active',)
    raw_id_fields = ('user', 'product')
    list_filter = ('is_active', 'created_at')
    list_per_page = 20