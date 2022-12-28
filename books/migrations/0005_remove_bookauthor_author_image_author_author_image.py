# Generated by Django 4.1.3 on 2022-11-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_bookauthor_author_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookauthor',
            name='author_image',
        ),
        migrations.AddField(
            model_name='author',
            name='author_image',
            field=models.ImageField(default='default_author.png', upload_to=''),
        ),
    ]
