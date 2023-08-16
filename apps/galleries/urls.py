from django.urls import path, include
from rest_framework.routers import DefaultRouter

from galleries.views.category import CategoryCreateAPIView, CategoryListAPIView, CategoryRetrieveAPIView
from galleries.views.gallery import GalleryModelViewSet

router = DefaultRouter()
router.register('', GalleryModelViewSet, 'gallery')
urlpatterns = [
    path('category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    path('', include(router.urls)),
]
