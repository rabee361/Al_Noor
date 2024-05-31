# Generated by Django 5.0.4 on 2024-05-30 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0047_secondarysteps_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='hajsteps',
            name='rank',
            field=models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
