# Generated by Django 4.1.3 on 2022-12-10 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0007_movie_bought_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="added_by",
            new_name="user",
        ),
    ]
