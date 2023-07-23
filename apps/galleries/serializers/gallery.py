from rest_framework.serializers import ModelSerializer

from galleries.models import Gallery


class GalleryModelSerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
