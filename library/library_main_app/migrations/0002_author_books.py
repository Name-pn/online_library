# Generated by Django 5.0.4 on 2024-04-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library_main_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="books",
            field=models.ManyToManyField(
                related_name="authors", to="library_main_app.book"
            ),
        ),
    ]
