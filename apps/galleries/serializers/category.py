from rest_framework.serializers import ModelSerializer

from galleries.models import Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        exclude = ('author',)

    def validate(self, attrs):
        request = self.context['request']
        attrs['author'] = request.user
        return attrs

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context['request']
        rep['author'] = request.user

        return rep
