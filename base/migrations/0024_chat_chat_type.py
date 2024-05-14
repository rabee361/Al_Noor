# Generated by Django 5.0.4 on 2024-05-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_basenotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_type',
            field=models.CharField(choices=[('guide', 'guide'), ('manager', 'manager')], default='guide', max_length=20),
        ),
    ]
