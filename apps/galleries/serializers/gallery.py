from rest_framework.fields import FileField
from rest_framework.serializers import ModelSerializer

from galleries.models import Gallery


class GalleryModelSerializer(ModelSerializer):
    file = FileField(required=True, read_only=False)

    class Meta:
        model = Gallery
        fields = ('description', 'file', 'category')
