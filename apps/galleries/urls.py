from django.urls import path, include
from rest_framework.routers import DefaultRouter

from galleries.views.category import CategoryCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, CategoryListAPIView
from galleries.views.gallery import GalleryModelViewSet, GalleryCreateAPIView

router = DefaultRouter()
router.register('', GalleryModelViewSet, 'gallery')
urlpatterns = [
    path('create/', GalleryCreateAPIView.as_view(), name='create'),
    path('category-detail/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('', include(router.urls)),
]
