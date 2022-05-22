from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
CHOICES = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Администратор'),
)


class CustomUser(AbstractUser):
    """Кастомная модель пользователя основанная на AbstractUser."""
    username = models.CharField(
        'Имя пользователя', max_length=150, unique=True,
        validators=[MinLengthValidator(5, message='Минимум 5 символов')])
    email = models.EmailField('Email адрес', unique=True)
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    date_joined = models.DateTimeField('Дата создания', default=timezone.now)
    bio = models.CharField('Биография', max_length=200, blank=True)
    role = models.CharField(
        'Роль',
        choices=CHOICES,
        max_length=10,
        default=USER,
        error_messages={'role': 'Выбрана несуществующая роль'}
    )
    confirmation_code = models.CharField(
        'Код подтверждения', blank=True, max_length=128
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def set_confirmation_code(self, confirmation_code):
        """Установка confirmation_code"""
        self.confirmation_code = confirmation_code

    @property
    def is_user(self):
        """Проверить является ли пользователь 'user'."""
        return self.role == USER

    @property
    def is_moderator(self):
        """Проверить является ли пользователь 'moderator'."""
        return self.role == MODERATOR

    @property
    def is_admin(self):
        """Проверить является ли пользователь 'admin'."""
        return self.role == ADMIN

    def __str__(self):
        return f'{self.username}, {self.email}'
