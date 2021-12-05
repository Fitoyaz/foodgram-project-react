# Generated by Django 3.2.9 on 2021-11-28 16:31

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20211128_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='', upload_to=recipes.models.Recipe.file_name, validators=[recipes.models.Recipe.validate_image], verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
