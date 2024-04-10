# Generated by Django 5.0.4 on 2024-04-09 13:03

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_main_app', '0006_author_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('books', models.ManyToManyField(blank=True, related_name='books_by_genre', to='library_main_app.book')),
            ],
        ),
    ]
