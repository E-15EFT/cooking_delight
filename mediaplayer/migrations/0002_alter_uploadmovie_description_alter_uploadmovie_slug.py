# Generated by Django 5.0.2 on 2024-03-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaplayer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmovie',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='uploadmovie',
            name='slug',
            field=models.SlugField(max_length=1300, unique=True),
        ),
    ]
