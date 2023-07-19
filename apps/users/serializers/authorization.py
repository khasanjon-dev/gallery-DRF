from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer, CharField

from users.models import User
from utils.validatiors import is_phone_number_valid, generate_correct_phone_number


class MainSerializer(Serializer):
    @staticmethod
    def validate_phone_exists(phone):
        user = User.objects.filter(phone=phone).first()
        if not user:
            raise ValidationError('Bunday raqam topilmadi !')  # noqa
        return user

    @staticmethod
    def get_user_by_phone(phone):
        user = User.objects.filter(phone=phone).first()
        return user


class CodeSendSerializer(MainSerializer):
    phone = CharField(max_length=12)

    def validate(self, attrs):
        phone = attrs.get('phone')
        valid, msg = is_phone_number_valid(phone)
        if not valid:
            raise ValidationError("Telefon raqam to'g'ri kiriting !")
        c_p = generate_correct_phone_number(msg)
        self.validate_phone_exists(c_p)
        attrs['phone'] = c_p
        return attrs

    @staticmethod
    def validate_phone_exists(phone):
        user = User.objects.filter(phone=phone, is_active=True)
        if user:
            raise ValidationError("Bu raqam allaqachon ro'yxatdan o'tgan !")


class CodeCheckSerializer(Serializer):
    code = CharField(max_length=6)
    phone = CharField(max_length=12)

    def validate(self, attrs):
        code = attrs.get('code', None)
        phone = attrs.get('phone')
        if not phone or not code:
            raise ValidationError('Telefon raqam va kod kiritilishi kerak!')

        valid, msg = is_phone_number_valid(phone)
        if not valid:
            raise ValidationError("Telefon raqam to'g'ri yozing!")
        c_p = generate_correct_phone_number(phone)
        attrs['phone'] = c_p
        if not code == cache.get(phone):
            raise ValidationError('Kod mos kelmadi!')
        else:
            cache.delete(phone)
        return attrs


class RegisterSerializer(MainSerializer):
    first_name = CharField(max_length=250)
    phone = CharField(max_length=12)
    password = CharField(max_length=100)

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
        first_name = attrs.get('first_name')
        if not phone or not password or not first_name:
            raise ValidationError('Telefon raqam, parol, ism kiritilishi majburiy!')
        if len(password) < 5:
            raise ValidationError("Parol kamida 5 ta belgidan iborat bo'lishi kerak!")
        valid, msg = is_phone_number_valid(phone)
        if not valid:
            raise ValidationError("Telefon raqam to'g'ri kiriting!")

        c_p = generate_correct_phone_number(msg)
        user = self.get_user_by_phone(c_p)
        if user.first_name and user.is_active:
            raise ValidationError("Bu raqam oldin ro'yxatdan o'tgan!")
        self.save_user(user, first_name, password)
        return attrs

    @staticmethod
    def save_user(user, first_name, password):
        user.first_name = first_name
        user.set_password(password)
        user.is_active = True
        user.save()
