from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=40, verbose_name='Заголовок')
    preview = models.TextField(max_length=250, verbose_name='Краткое содержание')
    content = models.TextField(verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/news/%Y/%m/%d', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey('NewsCategory', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class NewsCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']