from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import UpdateModel, CreateModel
from mptt.models import MPTTModel, TreeForeignKey


class Rate(models.Model):
    class RateChoose(models.TextChoices):
        one = 'one'
        tow = 'tow'
        three = 'three'
        four = 'four'
        five = 'five'
    rate_choose = models.CharField(max_length=5, choices=RateChoose.choices, default=RateChoose.five)

    def __str__(self) -> str:
        return self.rate_choose
    
    class Meta:
        abstract = True


class RelationUser(models.Model):
    class RelationUserChoose(models.TextChoices):
        like = 'like'
        dislike = 'dislike'
    relation_choose = models.CharField(max_length=7, choices=RelationUserChoose.choices, default=None,
                                       blank=True)

    def __str__(self) -> str:
        return self.relation_choose
    
    class Meta:
        abstract = True


class CommentProduct(CreateModel, Rate):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='user_comment')
    product = models.ForeignKey('products.ProductModel', on_delete=models.PROTECT, related_name='product_comments')
    title_comment = models.CharField(max_length=50)
    text_comment = models.TextField(max_length=500)
    is_active =models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title_comment
    
    class Meta:
        db_table = 'comment'
        
    
class QuestionModel(CreateModel):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='user_questions')
    product = models.ForeignKey('products.ProductModel', on_delete=models.PROTECT, related_name='product_questions')
    body_question = models.TextField(max_length=500)
    is_active =models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.body_question[:30]

    class meta:
        db_table = 'question'

class AnswerProduct(MPTTModel, RelationUser, CreateModel):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='user_answers')
    question = models.ForeignKey(QuestionModel, on_delete=models.PROTECT, related_name='questions')
    product = models.ForeignKey('products.ProductModel', on_delete=models.PROTECT, related_name='product_answers')
    answer_body = models.TextField(max_length=500)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active =models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.answer_body[:30]
    
    class meta:
        db_table = 'answer'