# Generated by Django 5.0.4 on 2024-04-17 08:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_hajsteps_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hajsteps',
            options={'verbose_name': 'خطوة', 'verbose_name_plural': 'خطوات الأعمال الديني'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
