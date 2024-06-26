# Generated by Django 5.0.4 on 2024-05-20 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_alter_pilgrim_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilgrim',
            name='guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.guide', verbose_name='المرشد'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='tradition_reference',
            field=models.CharField(verbose_name='مرجع التقليد'),
        ),
    ]
