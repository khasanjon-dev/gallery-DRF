from django.db.models import Model, CharField, ForeignKey, CASCADE

from users.models import User


class Category(Model):
    name = CharField(max_length=250)

    def __str__(self):
        return self.name


class UserCategory(Model):
    # relationship
    user = ForeignKey(User, CASCADE)
    category = ForeignKey(Category, CASCADE)

    def __str__(self):
        return self.user.first_name + '-' + self.category.name

    class Meta:
        unique_together = ['user', 'category']
