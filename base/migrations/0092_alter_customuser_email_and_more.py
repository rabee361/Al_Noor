# Generated by Django 5.1.3 on 2025-05-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0091_alter_pilgrim_room_num"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                blank=True,
                default="Info@alnoor-hajj.com",
                max_length=254,
                null=True,
                verbose_name="الايميل",
            ),
        ),
        migrations.AlterField(
            model_name="pilgrim",
            name="registeration_id",
            field=models.CharField(max_length=50, verbose_name="رقم الهوية"),
        ),
    ]
