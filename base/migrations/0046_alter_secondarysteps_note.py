# Generated by Django 5.0.4 on 2024-05-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0045_remove_hajsteps_note_secondarysteps_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondarysteps',
            name='note',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='ملاحظة'),
        ),
    ]
