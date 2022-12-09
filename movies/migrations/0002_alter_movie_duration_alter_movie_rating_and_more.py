# Generated by Django 4.1.3 on 2022-12-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.CharField(
                choices=[
                    ("G", "General Audience"),
                    ("PG", "Parental Guidance Suggested"),
                    ("PG-13", "Parents Strongly Cautioned"),
                    ("R", "Restricted"),
                    ("NC-17", "No One 17 And Under Admitted"),
                ],
                default="G",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(default=None, null=True),
        ),
    ]
