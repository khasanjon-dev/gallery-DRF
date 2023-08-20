from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from galleries.models import Category
from galleries.serializers.category import CategoryCreateSerializer, CategoryListRetrieveUpdateSerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRetrieveUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        category = Category.objects.filter(author_id=user.id)
        return category


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRetrieveUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        category = Category.objects.filter(author_id=user.id)
        return category
