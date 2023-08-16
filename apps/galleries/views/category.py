from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView

from galleries.models import Category
from galleries.serializers.category import CategoryCreateModelSerializer, CategoryListModelSerializer, \
    CategoryUpdateModelSerializer, CategoryRetrieveModelSerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateModelSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListModelSerializer

    def get_queryset(self):
        user = self.request.user
        category = Category.objects.filter(author_id=user.id)
        return category


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveModelSerializer

    def get_queryset(self):
        user = self.request.user
        category = Category.objects.filter(author_id=user.id)
        return category


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateModelSerializer
