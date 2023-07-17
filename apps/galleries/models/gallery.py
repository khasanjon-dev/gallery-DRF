from django.db.models import Model, CharField, FileField


class Gallery(Model):
    name = CharField(max_length=255)
    file = FileField(upload_to='gallery')
