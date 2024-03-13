from django.db import models
from django.utils.text import slugify

NULLABLE = {
    'blank': True,
    'null': True
}


class User(models.Model):
    first_name = models.CharField(**NULLABLE, max_length=30, verbose_name='Имя')
    last_name = models.CharField(**NULLABLE, max_length=30, verbose_name='Фамилия')
    age = models.IntegerField(**NULLABLE, verbose_name='Возраст')
    photo = models.ImageField(**NULLABLE, upload_to='user/', verbose_name='Фото')
    email = models.EmailField(**NULLABLE, verbose_name='Почта')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(**NULLABLE, upload_to='category/', verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class Dog(models.Model):
    name = models.CharField(max_length=50, verbose_name='Кличка')
    age = models.IntegerField(**NULLABLE, verbose_name='Возраст')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(**NULLABLE, upload_to='dog/', verbose_name='Фото')
    price = models.IntegerField(verbose_name='Стоимость')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Порода')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    photo = models.ImageField(**NULLABLE, upload_to='blog_previews/', verbose_name='Превью')
    view_count = models.IntegerField(default=0, verbose_name='Просмотры')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=False, verbose_name='Публикация')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
