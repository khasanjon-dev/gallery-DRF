from django.db.models import Model, CharField, ForeignKey, CASCADE

from galleries.models import Category
from users.models import User


class UserCategory(Model):
    user = ForeignKey(User, CASCADE)
    category = ForeignKey(Category, CASCADE)
    author = ForeignKey(user, CASCADE)
