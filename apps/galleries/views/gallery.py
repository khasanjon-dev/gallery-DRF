from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from galleries.models import Gallery
from galleries.serializers.gallery import GalleryModelSerializer, GalleryCreateSerializer


class GalleryModelViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GalleryModelSerializer


class GalleryCreateAPIView(CreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryCreateSerializer


