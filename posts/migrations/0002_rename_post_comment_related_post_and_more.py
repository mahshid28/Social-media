# Generated by Django 4.2.1 on 2023-06-20 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="post",
            new_name="related_post",
        ),
        migrations.RenameField(
            model_name="like",
            old_name="post",
            new_name="related_post",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="like",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="post",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="post",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="comment",
            name="reply_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.comment",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name="Content"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50)),
                (
                    "related_post",
                    models.ManyToManyField(related_name="tags", to="posts.post"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PostImage",
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
                ("image", models.ImageField(upload_to="uploads/photos/")),
                (
                    "related_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.post"
                    ),
                ),
            ],
            options={
                "verbose_name": "Like",
                "verbose_name_plural": "Likes",
            },
        ),
    ]