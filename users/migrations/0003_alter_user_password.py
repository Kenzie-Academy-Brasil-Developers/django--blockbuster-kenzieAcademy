# Generated by Django 4.1.3 on 2022-12-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_birthdate_user_is_employee_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=127),
        ),
    ]
