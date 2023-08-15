from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from galleries.models import Category


# class CategoryCreateModelSerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         exclude = ('author',)
#
#     def validate(self, attrs):
#         request = self.context['request']
#         author = attrs['author'] = request.user
#         name = attrs['name']
#         user_id = attrs['user'][0]
#         if Category.objects.filter(author__category__author_id=author.id, name=name,
#                                    user__categories__user__=user_id).exists():
#             raise ValidationError('Sizda bunday kategoriya allaqachon mavjud !')
#
#         return attrs
#
#
# class CategoryUserListModelSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class CategoryCreateModelSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Category
        fields = ('name', 'author')


class CategoryListModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'author')
