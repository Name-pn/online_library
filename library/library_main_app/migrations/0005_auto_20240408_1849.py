# Generated by Django 5.0.4 on 2024-04-08 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_main_app', '0004_alter_author_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',

        )
    ]
