from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from galleries.models import Category
from galleries.serializers.category import CategoryModelSerializer
from shared.django_restframework.permission import IsOwner


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsOwner, IsAuthenticated)
