from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from galleries.models import Gallery
from galleries.serializers.gallery import GalleryModelSerializer
from shared.django_restframework.permission import IsOwner


class GalleryModelViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GalleryModelSerializer
    permission_classes = (IsOwner, IsAuthenticatedOrReadOnly)
