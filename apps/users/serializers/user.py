from collections import defaultdict

from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer, CharField

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'phone',
            'email',
            'photo',
            'password'
        )

    def validate(self, attrs):
        errors = defaultdict(list)

        if password := attrs.get('password'):
            attrs['password'] = make_password(password)

        if User.objects.filter(phone=attrs['phone']).exists():
            errors['phone'].append('Phone number has already taken')
        if errors:
            raise ValidationError(errors)
        return attrs


class SendCodeSerializer(Serializer):
    phone = CharField(max_length=12)

    def validate(self, attrs):
        phone = attrs.get('phone')
