from django.db.models import Model, CharField, ManyToManyField, ForeignKey, CASCADE

from users.models import User


class Category(Model):
    name = CharField(max_length=250)
    user = ManyToManyField(User)
    author = ForeignKey(User, CASCADE, related_name='categories')

    def __str__(self):
        return self.name
