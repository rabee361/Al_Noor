# Generated by Django 5.1.3 on 2025-04-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0085_registration_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="pilgrim",
            name="email",
            field=models.EmailField(
                blank=True,
                default="info@alnoor-hajj.com",
                max_length=254,
                null=True,
                verbose_name="الايميل",
            ),
        ),
        migrations.AlterField(
            model_name="registration",
            name="email",
            field=models.EmailField(
                blank=True,
                default="Info@alnoor-hajj.com",
                max_length=254,
                null=True,
                verbose_name="الايميل",
            ),
        ),
    ]
