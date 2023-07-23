from django.db.models import Model, CharField, FileField, DateTimeField, ForeignKey, CASCADE


class Gallery(Model):
    name = CharField(max_length=255)
    file = FileField(upload_to='gallery')
    updated_at = DateTimeField(auto_now=True, null=True)
    created_at = DateTimeField(auto_now_add=True)

    # relationship
    category = ForeignKey('Category', CASCADE)
