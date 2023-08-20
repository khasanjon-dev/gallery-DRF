from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from galleries.models import Category


class CategoryCreateSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Category
        fields = ('name', 'author')


class CategoryListRetrieveUpdateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'author')
