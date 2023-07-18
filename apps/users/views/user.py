from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet

from shared.django_restframework.permission import IsOwner
from users.models import User
from users.serializers.authorization import CodeSendSerializer
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
        # try:
        #     code = generate_code()
        #     user = User.objects.create_user()
