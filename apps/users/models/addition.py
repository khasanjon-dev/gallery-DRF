from django.db.models import Model, ForeignKey, CASCADE

from galleries.models import Gallery, Category
from users.models import User


class Favorite(Model):
    # relationship
    media = ForeignKey(Gallery, CASCADE)
    author = ForeignKey(User, CASCADE)


class UserCategory(Model):
    # relationship
    user = ForeignKey(User, CASCADE)
    category = ForeignKey(Category, CASCADE)
