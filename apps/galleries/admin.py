from django.contrib import admin
from django.contrib.admin import ModelAdmin

from galleries.models import Gallery, Category


@admin.register(Gallery)
class GalleryModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass
