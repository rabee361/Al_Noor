# Generated by Django 5.0.4 on 2024-04-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_pilgrim_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='employee',
            field=models.BooleanField(default=False),
        ),
    ]