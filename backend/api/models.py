import os

from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.utils.html import format_html


class UserRole(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    color = models.CharField(max_length=7, verbose_name='Цвет')
    slug = models.SlugField(verbose_name='Слаг')

    def color_name(self):
        return format_html(
            '<span style="color: {};">Текст</span>',
            self.color,
        )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тег'

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscriptions',
                             verbose_name='Пользователь')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_subscriptions',
                               verbose_name='Автор')

    def get_recipes(self):
        return Recipe.objects.select_related('author').filter(
            author__username=self.author)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'],
                                    name='unique_subscription'),
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Ingredient(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    measurement_unit = models.CharField(max_length=64, verbose_name='Единицы измерения')

    def __str__(self):
        return '{}, {}'.format(self.name, self.measurement_unit)

    class Meta:
        verbose_name = 'Ингредиенты'
        verbose_name_plural = 'Ингредиенты'


class Recipe(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        kilobyte_limit = settings.RECIPE_IMAGE_LIMIT
        if filesize > kilobyte_limit * 1024:
            raise ValidationError(
                'Максимальный размер изображения %s Kbyte' % str(
                    kilobyte_limit))

    def file_name(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{instance.slug}.{ext}'
        fullname = os.path.join(settings.MEDIA_ROOT, 'images/', filename)
        if os.path.exists(fullname):
            os.remove(fullname)

        return f'images/{filename}'

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipes', verbose_name='Автор')
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to='recipes/', validators=[validate_image],
                              verbose_name='Изображение', )
    text = models.TextField(verbose_name='Описание')

    ingredients = models.ManyToManyField(Ingredient,
                                         through='IngredientAmount')
    tags = models.ManyToManyField(Tag, verbose_name='Тег')
    # pub_date = models.DateTimeField(auto_now=True,
    #                                verbose_name='Дата добавления')

    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления (мин.)')
    #slug = models.SlugField(editable=False, unique=True,
    #                        verbose_name='Слаг')

    #@property
    def __str__(self):
        return '{}, {}'.format(self.name, self.cooking_time)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   verbose_name='Ингредиент')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    amount = models.PositiveIntegerField(verbose_name='Кол-во')

    #def __str__(self):
    #    return '{}, {}'.format(self.ingredient, self.amount)

    class Meta:
        verbose_name = 'Добавить ингредиент'
        verbose_name_plural = 'Ингредиенты для рецепта'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites',
                             verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorites', verbose_name='Рецепт')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_favorite'),
        ]
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='cart',
                             verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='cart',
                               verbose_name='Рецепт')

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_cart_list'),
        ]
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
