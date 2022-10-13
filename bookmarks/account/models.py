from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)