from rest_framework.exceptions import ValidationError
from rest_framework.fields import FileField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from galleries.models import Gallery, Category


class GalleryModelSerializer(ModelSerializer):
    file = FileField(required=True, read_only=False)

    class Meta:
        model = Gallery
        fields = ('description', 'file', 'category')


class GalleryCreateSerializer(ModelSerializer):
    file = FileField(required=True, read_only=False)
    author = HiddenField(default=CurrentUserDefault())

    def validate(self, attrs):
        category = attrs['category']
        author = attrs['author']
        if not Category.objects.filter(pk=category.id, author=author).exists():
            raise ValidationError('Validation Error something mistake by user !')
        return attrs

    class Meta:
        model = Gallery
        fields = ('description', 'file', 'category', 'author')
