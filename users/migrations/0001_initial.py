# Generated by Django 4.2.1 on 2023-06-13 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                    "bio",
                    models.CharField(blank=True, max_length=300, verbose_name="Bio"),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, upload_to="profile_pics", verbose_name="Profile_pic"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Phone_number"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
            },
        ),
    ]
