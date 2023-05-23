import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    uuid = models.UUIDField(
        'uuid',
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Audio(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='audios'
    )
    uuid = models.UUIDField(
        'audio_uuid',
        default=uuid.uuid4,
        unique=True
    )
    file = models.FileField('mp3_audio', upload_to='records/')

    class Meta:
        verbose_name = 'Аудиозапись'
        verbose_name_plural = 'Аудиозаписи'
