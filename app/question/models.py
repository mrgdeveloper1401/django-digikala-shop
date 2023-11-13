from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import UpdateModel, CreateModel


class CommentProduct(CreateModel):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='user_comment')
    product = models.ForeignKey('products.ProductModel', on_delete=models.PROTECT, related_name='product_comments')
    title_comment = models.CharField(_('عنوان نظر'), max_length=50)
    text_comment = models.TextField(_('نظر'), max_length=500)
    
    def __str__(self) -> str:
        return self.title_comment
    
    class Meta:
        verbose_name = _('نظر')
        verbose_name_plural = _('نظرها')
        db_table = 'comment'
        
    
class QuestionModel(CreateModel):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='user_questions')
    product = models.ForeignKey('products.ProductModel', on_delete=models.PROTECT, related_name='product_questions')
    body_question = models.TextField(_('متن سوال'), max_length=500)
    
    def __str__(self) -> str:
        return self.body_question[:30]


class AnswerProduct(CreateModel):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='user_answers')
    question = models.ForeignKey('products.QuestionModel', on_delete=models.PROTECT, related_name='question_answers')
    product = models.ForeignKey('products.ProductModel', on_delete=models.PROTECT, related_name='product_answers')
    answer_body = models.TextField(_('متن پاسخ'), max_length=500)
    
    def __str__(self) -> str:
        return self.answer_body[:30]
    
    class meta:
        verbose_name = _('پاسخ')
        verbose_name_plural = _('پاسخ ها')
        db_table = 'answer'