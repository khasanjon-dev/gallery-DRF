from rest_framework.viewsets import ModelViewSet

from galleries.models import Category
from galleries.serializers.category import CategoryModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
