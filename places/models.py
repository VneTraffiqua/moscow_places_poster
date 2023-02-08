from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Место',
        help_text='Введите название места',
        unique=True,
    )
    short_description = models.CharField(
        verbose_name='Короткое описание',
        max_length=255,
        help_text='Введите короткое описание',
        null=True,
        blank=True
    )
    long_description = HTMLField(
        verbose_name='Описание',
        help_text='Введите описание',
        null=True,
        blank=True
    )
    lat = models.FloatField(max_length=20, unique=True)
    lon = models.FloatField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Photo(models.Model):
    image = models.ImageField(
        upload_to='media/', verbose_name='Изображение', unique=True
    )
    place = models.ForeignKey(
        Place, related_name='photos',
        on_delete=models.CASCADE,
        null=True
    )
    number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id} {self.place}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['place']
