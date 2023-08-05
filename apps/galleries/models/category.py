from django.db.models import Model, CharField, ForeignKey, CASCADE, SET_NULL

from users.models import User


class Category(Model):
    name = CharField(max_length=250)
    author = ForeignKey(User, CASCADE)
    user = ForeignKey(User, SET_NULL)

    class Meta:
        unique_together = ('name', 'author', 'user')

    def __str__(self):
        return self.name
