# Generated by Django 5.0.4 on 2024-04-06 18:29

import uuid
from django.db import migrations, models


def author_uuid_forward(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Author = apps.get_model('library_main_app', 'Author')
    for author in Author.objects.using(db_alias).all():
        author.uuid = uuid.uuid4()
        author.save()


class Migration(migrations.Migration):

    dependencies = [
        ('library_main_app', '0002_author_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='uuid',
            field=models.UUIDField(null=True)
        ),
        migrations.RunPython(author_uuid_forward),
        migrations.AlterField(
            model_name='author',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, serialize=False),
        ),
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='uuid',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True),
        ),
    ]
