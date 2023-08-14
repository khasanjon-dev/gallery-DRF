from django.db.models import Model, ForeignKey, CASCADE, SET_NULL

from galleries.models import Category
from users.models import User


class UserCategory(Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    category = ForeignKey(Category, CASCADE)
    author = ForeignKey(User, CASCADE, related_name='categories')
