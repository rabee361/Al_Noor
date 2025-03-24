# Generated by Django 5.1.3 on 2025-03-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0081_livestream_rank"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livestream",
            name="description",
        ),
        migrations.AddField(
            model_name="livestream",
            name="content",
            field=models.TextField(default=" ", verbose_name="المحتوى"),
            preserve_default=False,
        ),
    ]
