from django.conf import settings
from django.utils.crypto import get_random_string
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase

from users import serializers
from users.models import CustomUser
from users.permissions import AdminOnly


class UserViewSet(viewsets.ModelViewSet):
    """CRUD user models."""
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, AdminOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['username']
    lookup_field = 'username'

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        detail=False,
        methods=['get', 'put', 'patch'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        """API для редактирования текущим пользователем своих данных."""
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(role=user.role, partial=True)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenSerializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def get_confirmation_code(request):
    """
    Получить код подтверждения и пароль на переданный email.
    Поля email и username должны быть уникальными.
    """
    serializer = serializers.UserRegistationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = CustomUser.objects.create(
        username=serializer.validated_data['username'],
        email=serializer.validated_data['email'],
    )
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    confirmation_code = get_random_string(18, chars)
    user.set_confirmation_code(confirmation_code=confirmation_code)
    user.save()
    user.email_user(
        subject='Создан confirmation code для получения token',
        message=f'Ваш confirmation code: {confirmation_code}',
        from_email=settings.EMAIL_HOST_USER,
    )
    return Response(serializer.validated_data, status=status.HTTP_200_OK)


class CustomTokenView(TokenViewBase):
    """Получение токена взамен username и confirmation code."""
    serializer_class = serializers.CustomTokenSerializer
    permission_classes = [AllowAny]
