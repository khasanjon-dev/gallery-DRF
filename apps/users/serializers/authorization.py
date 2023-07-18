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
