from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from galleries.models import Category


class CategoryCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('author',)

    def validate(self, attrs):
        request = self.context['request']
        author = attrs['author'] = request.user
        name = attrs['name']
        user_id = attrs['user'][0]
        if Category.objects.filter(author__category__author_id=author.id, name=name,
                                   user__categories__user__=user_id).exists():
            raise ValidationError('Sizda bunday kategoriya allaqachon mavjud !')

        return attrs


class CategoryListModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, attrs):
        request = self.context['request']
        # if Category.objects.filter(author__category__author_id=request.user.id).exists():
        #     Category.objects.
