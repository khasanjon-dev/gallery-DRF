from django.urls import path
from rest_framework.routers import DefaultRouter

from galleries.views.category import CategoryCreateAPIView, CategoryListAPIView
from galleries.views.gallery import GalleryModelViewSet

router = DefaultRouter()
router.register('', GalleryModelViewSet, 'gallery')

urlpatterns = [
    # path('', include(router.urls)),
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
]
