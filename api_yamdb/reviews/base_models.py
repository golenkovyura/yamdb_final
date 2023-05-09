from django.conf import settings
from django.db import models

from users.models import User


class BaseModelGenreCategory(models.Model):
    """Абстрактная модель для жанров и категорий."""

    name = models.CharField('Название', max_length=settings.LEN_FOR_NAME)
    slug = models.SlugField('Ссылка',
                            max_length=settings.LEN_FOR_SLUG,
                            unique=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name


class BaseReviewCommentModel(models.Model):
    """Базовый абстрактный класс для Review и Comment."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.text[:settings.CUT_TEXT]
