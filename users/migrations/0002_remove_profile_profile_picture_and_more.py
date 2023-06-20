# Generated by Django 4.2.1 on 2023-06-20 12:44

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="profile_picture",
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=11, verbose_name="Phone_number"
            ),
        ),
        migrations.CreateModel(
            name="Relation",
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
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follower",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="following",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
            },
            bases=(models.Model, core.models.TimeStampMixin),
        ),
        migrations.CreateModel(
            name="ProfilePic",
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
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        upload_to="uploads/photos/",
                        verbose_name="Profile_picture",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]