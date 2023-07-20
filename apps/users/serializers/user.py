from collections import defaultdict

from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer, CharField

from users.models import User
from utils.validatiors import phone_regex


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'image',
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


class UserUpdateModelSerializer(ModelSerializer):
    phone = CharField(max_length=12, validators=[phone_regex], read_only=True)
    password = CharField(write_only=True, required=False, min_length=5)
    image = ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'password',
            'image'
        )

    def validate(self, attrs):
        if password := attrs.get('password'):
            attrs['password'] = make_password(password)
        return attrs
