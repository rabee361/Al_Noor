# Generated by Django 5.0.4 on 2024-04-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_ahkamalmrah_pilgrim_ahkamalmrah_typeahkamalmrah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilgrim',
            name='ahkamalmrah',
            field=models.ManyToManyField(blank=True, null=True, to='base.ahkamalmrah'),
        ),
    ]
