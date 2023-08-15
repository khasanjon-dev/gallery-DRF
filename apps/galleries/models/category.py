from django.db.models import Model, CharField, ForeignKey, CASCADE

from users.models import User


class Category(Model):
    name = CharField(max_length=250)
    author = ForeignKey(User, CASCADE, related_name='category')

    class Meta:
        unique_together = ('name', 'author')

    def __str__(self):
        return self.name
