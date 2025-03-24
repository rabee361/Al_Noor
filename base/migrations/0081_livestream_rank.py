# Generated by Django 5.1.3 on 2025-03-24 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0080_livestreamcategory_alter_pilgrim_options_livestream"),
    ]

    operations = [
        migrations.AddField(
            model_name="livestream",
            name="rank",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(1000),
                ],
                verbose_name="الترتيب",
            ),
            preserve_default=False,
        ),
    ]
