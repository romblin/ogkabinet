from django.db import models
from django.contrib.auth import get_user_model

from kabinet.common.fields import OptionalCharField


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), verbose_name='Пользователь')
    first_name = OptionalCharField(verbose_name='Имя', max_length=150)
    phone = OptionalCharField(verbose_name='Телефон', max_length=20)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.phone)
