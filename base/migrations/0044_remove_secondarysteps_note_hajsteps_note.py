# Generated by Django 5.0.4 on 2024-05-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0043_userpassword_alter_pilgrim_haj_steps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondarysteps',
            name='note',
        ),
        migrations.AddField(
            model_name='hajsteps',
            name='note',
            field=models.CharField(default='note', max_length=500, verbose_name='ملاحظة'),
        ),
    ]
