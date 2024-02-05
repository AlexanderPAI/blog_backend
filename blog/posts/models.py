from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    """Модель поста."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста',
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок',
        help_text='Введите заголовок поста',
    )
    text = models.TextField(
        max_length=140,
        verbose_name='Текст поста',
        help_text='Напишите содержимое поста',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата создания поста',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
