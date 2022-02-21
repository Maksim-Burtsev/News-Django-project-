from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=250)

    content = models.TextField('Содержание')

    time_published = models.DateTimeField('Время публикации', blank=True)

    cat = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE, db_index=True, verbose_name='Категория')

    url = models.URLField('Ссылка')

    minutes_to_read = models.DecimalField(
        'Минут на прочтение', max_digits=3, decimal_places=1, blank=True, null=True)

    quantity_words = models.IntegerField(
        'Количество слов', blank=True, null=True
        )

    image_link = models.CharField('Ссылка на фото', max_length=250, blank=True)

    is_published = models.BooleanField('Опубликовать', default=True)

    def get_absolute_url():
        pass

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ['-time_published',]


class Category(models.Model):

    title = models.CharField('Категория', max_length=250)

    slug = models.SlugField('Slug', unique=True, blank=True, null=True)

    url = models.URLField('Ссылка')

    def __str__(self):
        return self.title

    def get_absolute_url():
        pass

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
