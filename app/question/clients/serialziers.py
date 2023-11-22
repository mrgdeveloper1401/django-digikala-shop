from rest_framework.serializers import ModelSerializer
from question.models import AnswerProduct, QuestionModel, CommentProduct


class ComentModelSerializer(ModelSerializer):
    class Meta:
        model = CommentProduct
        exclude = ('is_active', )


class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = QuestionModel
        exclude = ('is_active', )


class AnswerProductModelSerializer(ModelSerializer):
    class Meta:
        model = AnswerProduct
        exclude = ('is_active', )