# Generated by Django 5.1.3 on 2025-04-06 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0084_registration_createdat"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="email",
            field=models.EmailField(
                blank=True, default="Info@alnoor-hajj.com", max_length=254, null=True
            ),
        ),
    ]
