from django.urls import path, include
from rest_framework.routers import DefaultRouter

from galleries.views.category import CategoryModelViewSet

router = DefaultRouter()
router.register('category', CategoryModelViewSet, 'category')

urlpatterns = [
    path('', include(router.urls))
]
