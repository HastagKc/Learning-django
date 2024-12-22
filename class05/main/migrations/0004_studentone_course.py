# Generated by Django 4.2.17 on 2024-12-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_teachertable_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentOne",
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
                ("name", models.CharField(max_length=258)),
                ("age", models.IntegerField()),
                ("phone", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                ("subject", models.CharField(max_length=200)),
                ("student", models.ManyToManyField(to="main.studentone")),
            ],
        ),
    ]
