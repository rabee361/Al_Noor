# Generated by Django 5.1.3 on 2025-03-24 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0079_delete_userpassword"),
    ]

    operations = [
        migrations.CreateModel(
            name="LiveStreamCategory",
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
                ("name", models.CharField(max_length=50, verbose_name="الاسم")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="تاريخ الإنشاء"
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="pilgrim",
            options={"ordering": ["-id"]},
        ),
        migrations.CreateModel(
            name="LiveStream",
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
                ("cover", models.ImageField(upload_to="cover", verbose_name="الغلاف")),
                ("title", models.CharField(max_length=100, verbose_name="العنوان")),
                ("description", models.TextField(verbose_name="الوصف")),
                ("stream_url", models.URLField(verbose_name="رابط البث المباشر")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="تاريخ الإنشاء"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.livestreamcategory",
                        verbose_name="الفئة",
                    ),
                ),
            ],
        ),
    ]
