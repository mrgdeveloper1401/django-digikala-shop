from rest_framework.viewsets import ModelViewSet
from question.models import CommentProduct, QuestionModel, AnswerProduct
from .serialziers import ComentModelSerializer, QuestionModelSerializer, AnswerProductModelSerializer
from question.permission import IsOwner


class CommentModelViewSet(ModelViewSet):
    queryset = CommentProduct.objects.all()
    serializer_class = ComentModelSerializer
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class QuestionModelViewSet(ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionModelSerializer
    permission_classes = (IsOwner,)


class AnswerProductModelViewSet(ModelViewSet):
    queryset = AnswerProduct.objects.all()
    serializer_class = AnswerProductModelSerializer
    permission_classes = (IsOwner,)