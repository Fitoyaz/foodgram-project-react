# Generated by Django 3.2.9 on 2021-11-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20211128_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингредиенты', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Рецепты', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='recipe',
            name='tag',
            field=models.ManyToManyField(to='recipes.Tag', verbose_name='Тег'),
        ),
    ]
