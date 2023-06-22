from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError


class User(AbstractUser):
    """Модель пользователя."""
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    first_name = models.CharField('Имя',
                                  max_length=150)
    last_name = models.CharField('Фамилия',
                                 max_length=150)
    email = models.EmailField('Email',
                              unique=True,
                              max_length=200)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(fields=('username', 'email'),
                                    name='unique_user')
        ]

    def clean(self):
        if self.username == 'me':
            raise ValidationError(
                {'error': 'Невозможно создать пользователя с именем me'}
            )

    def __str__(self):
        return self.username


class Follow(models.Model):
    """
    Модель подписки на авторов.
    Подписаться на себя нельзя.
    """
    username = models.ForeignKey(User,
                                 related_name='followers',
                                 verbose_name='Подписчик',
                                 on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               related_name='followings',
                               verbose_name='Автор',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=['username', 'author'],
                                    name='unique_follower')
        ]

    def clean(self):
        if self.username == self.author:
            raise ValidationError(
                {'error': 'Невозможно подписаться на себя'}
            )

    def __str__(self):
        return f'Автор: {self.author}, подписчик: {self.user}'
