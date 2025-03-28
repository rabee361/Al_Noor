# Generated by Django 5.1.3 on 2025-03-28 12:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0083_customuser_is_deleted_registration_is_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="createdAt",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="تاريخ التسجيل",
            ),
            preserve_default=False,
        ),
    ]
