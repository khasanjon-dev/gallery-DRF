from django.urls import path, include
from rest_framework.routers import DefaultRouter

from galleries.views.category import CategoryModelViewSet
from galleries.views.gallery import GalleryModelViewSet

router = DefaultRouter()
router.register('category', CategoryModelViewSet, 'category')
router.register('', GalleryModelViewSet, 'gallery')

urlpatterns = [
    path('', include(router.urls))
]
