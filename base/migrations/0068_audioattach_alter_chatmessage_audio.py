# Generated by Django 5.0.4 on 2024-11-23 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0067_alter_basenotification_sentby_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioAttach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='audio/chats')),
            ],
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='audio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.audioattach'),
        ),
    ]
