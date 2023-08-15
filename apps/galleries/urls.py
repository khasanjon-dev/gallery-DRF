from django.urls import path, include
from rest_framework.routers import DefaultRouter

from galleries.views.category import CategoryCreateAPIView
from galleries.views.gallery import GalleryModelViewSet

router = DefaultRouter()
router.register('', GalleryModelViewSet, 'gallery')
urlpatterns = [
    path('category-create', CategoryCreateAPIView.as_view(), name='category-create'),
    path('', include(router.urls)),
]
