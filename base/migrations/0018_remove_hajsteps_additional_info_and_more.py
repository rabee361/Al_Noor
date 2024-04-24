# Generated by Django 5.0.4 on 2024-04-24 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_secondarysteps_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hajsteps',
            name='additional_info',
        ),
        migrations.RemoveField(
            model_name='hajsteps',
            name='description',
        ),
        migrations.AddField(
            model_name='task',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='تم قبولها'),
        ),
    ]
