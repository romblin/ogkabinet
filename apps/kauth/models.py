from django.contrib.auth.models import AbstractUser

from kabinet.common.fields import OptionalCharField


class KUser(AbstractUser):
    first_name = OptionalCharField('Имя', max_length=150)
    phone = OptionalCharField('Телефон', max_length=15)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
