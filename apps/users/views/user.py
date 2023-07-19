from django.core.cache import cache
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from root import settings
from shared.django_restframework.permission import IsOwner
from users.models import User
from users.serializers.authorization import CodeSendSerializer, CodeCheckSerializer, RegisterSerializer, \
    ChangePhoneSerializer, ChangePhoneConfirmSerializer
from users.serializers.user import UserModelSerializer
from utils.addtion import generate_code


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    ordering = ['-date_joined']

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=CodeSendSerializer)
    def send_code(self, request):
        """
        ## Sms yuborish uchun phone raqam yuboriladi
        ```
        {
            "phone": "998901001010"
        }
        ```
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get('phone', None)
        try:
            code = generate_code()
            user, created = User.objects.get_or_create(phone=phone)
            cache.set(user.phone, code, timeout=settings.REDIS_TIMEOUT)
            print(cache.get(user.phone))
            # TODO send phone code function
            # ...
        except Exception as e:
            detail = {
                'error': 'Sms yuborishda xatolik yuz berdi !',
                'detail': str(e)
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)
        detail = {
            'message': 'Sms successfully send!'
        }
        return Response(detail)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=CodeCheckSerializer)
    def check_code(self, request):
        """
        ## yuborilgan code ni tekshirish
        ```
        {
            "phone": "998901002020",
            "code": "200120"
        }
        ```
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        detail = {
            "message": "Sms successfully checked!"
        }
        return Response(detail)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=RegisterSerializer)
    def register(self, request):
        """
        ## bu urlga so'rov yuborishdan oldin quyidagilar ishlatilishi kerak
        ## users/send_code
        ## users/check_code
        ## register qismida first_name, password va phone yuboriladi
        ```
        {
            "phone_number": "998901001010",
            "first_name": "John",
            "password": "12345"
        }
        ```
        """

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False, permission_classes=(IsOwner,), serializer_class=ChangePhoneSerializer)
    def change_phone(self, request):
        """
        ## Telefon raqamni change qilish uchun api yangi telefon raqam yuboriladi
        ```
        {
            "phone": "998901001010"
        }
        ```
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data['phone']
        try:
            code = generate_code()
            user, created = User.objects.get_or_create(phone=phone)
            cache.set(user.phone, code, timeout=settings.REDIS_TIMEOUT)
            print(cache.get(user.phone))
            # TODO send phone code function
            # ...
        except Exception as e:
            detail = {
                'error': 'Sms yuborishda xatolik yuz berdi !',
                'detail': str(e)
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)
        detail = {
            'message': 'Sms successfully send!'
        }
        return Response(detail)

    @action(methods=['post'], detail=False, permission_classes=(IsOwner,),
            serializer_class=ChangePhoneConfirmSerializer)
    def change_phone_confirm(self, request):
        """
        ```
        {
            "phone": "998901001010",
            "code": "123456"
        }
        ```
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data['phone']
        if User.objects.filter(phone=phone).exists():
            detail = {
                'message': 'Bunday raqam mavjud!'
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)
        User.objects.filter(phone=request.user.phone).update(phone=phone)
        detail = {
            'message': 'Successfully changed!'
        }
        return Response(detail)

    @action(methods=['post'], detail=False, )
