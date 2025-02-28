# Generated by Django 4.2.17 on 2024-12-31 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("profile_img", models.ImageField(upload_to="media")),
                ("name", models.CharField(max_length=20)),
                ("title", models.CharField(max_length=100)),
                ("bio", models.CharField(max_length=200)),
            ],
        ),
    ]
