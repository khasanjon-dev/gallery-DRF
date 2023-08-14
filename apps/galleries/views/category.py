from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from galleries.models import Category


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category

    # @action(methods=['get'], detail=False, serializer_class=)
    # def get_category(self, request):
    #     """
    #     ## userning categoriya listini olish
    #     """
