from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from galleries.models import Category
from galleries.serializers.category import CategoryCreateModelSerializer, CategoryListModelSerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateModelSerializer
    permission_classes = (IsAuthenticated,)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        category = Category.objects.filter(author_id=user.id)
        return category
