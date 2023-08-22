from django.db.models import Model, FileField, DateTimeField, ForeignKey, CASCADE, TextField

from users.models import User
from utils.validatiors import custom_upload_to


class Gallery(Model):
    description = TextField(max_length=2000)
    file = FileField(upload_to=custom_upload_to)
    updated_at = DateTimeField(auto_now=True, null=True)
    created_at = DateTimeField(auto_now_add=True)

    # relationship
    category = ForeignKey('Category', CASCADE)
    author = ForeignKey(User, CASCADE)

    def __str__(self):
        return self.description
