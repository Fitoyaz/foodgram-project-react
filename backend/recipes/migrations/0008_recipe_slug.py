# Generated by Django 3.2.9 on 2021-11-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True, verbose_name='Слаг'),
            preserve_default=False,
        ),
    ]