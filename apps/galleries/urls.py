from django.urls import path, include
from rest_framework.routers import DefaultRouter

from galleries.views.category import CategoryModelViewSet
from galleries.views.gallery import GalleryModelViewSet

router = DefaultRouter()
router.register('', GalleryModelViewSet, 'gallery')
router.register('category', CategoryModelViewSet, 'category')

urlpatterns = [
    path('', include(router.urls)),
]
