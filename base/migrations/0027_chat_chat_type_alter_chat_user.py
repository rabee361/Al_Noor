# Generated by Django 5.0.4 on 2024-05-06 18:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_remove_registration_chronic_diseases_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_type',
            field=models.CharField(choices=[('guide', 'guide'), ('manager', 'manager')], default='guide', max_length=20),
        ),
        migrations.AlterField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المستخدم'),
        ),
    ]
