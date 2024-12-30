# Generated by Django 5.1.4 on 2024-12-23 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "properties",
            "0002_remove_property_likes_property_liked_by_chat_message_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="propertycomment",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="properties.propertycomment",
            ),
        ),
        migrations.CreateModel(
            name="CommentLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="properties.propertycomment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "comment")},
            },
        ),
        migrations.AddField(
            model_name="propertycomment",
            name="liked_by",
            field=models.ManyToManyField(
                related_name="liked_comments",
                through="properties.CommentLike",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
