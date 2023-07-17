from django.db.models import Model, ForeignKey, CASCADE

from galleries.models import Gallery
from users.models import User


class Favorite(Model):
    media = ForeignKey(Gallery, CASCADE)
    author = ForeignKey(User, CASCADE)
