# Generated by Django 4.2 on 2023-05-03 06:05

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
                ("name", models.CharField(max_length=1000)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
                ("summery", models.TextField()),
                ("degree", models.CharField(max_length=300)),
                ("school", models.CharField(max_length=2000)),
                ("university", models.CharField(max_length=500)),
                ("pervious_work", models.TextField(max_length=3000)),
                ("skill", models.TextField(max_length=2000)),
            ],
        ),
    ]
