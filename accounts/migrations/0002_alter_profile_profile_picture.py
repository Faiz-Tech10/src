# Generated by Django 5.1.4 on 2024-12-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(
                default="profile_pics/default.jpg", upload_to="profile_pics"
            ),
        ),
    ]
