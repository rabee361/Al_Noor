# Generated by Django 5.0.4 on 2024-05-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_guide_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='chronic_diseases',
        ),
        migrations.AlterField(
            model_name='registration',
            name='marital_status',
            field=models.CharField(choices=[('متزوج', 'متزوج'), ('أعزب', 'أعزب'), ('مطلق', 'مطلق')], max_length=10, verbose_name='الحالة الاجتماعية'),
        ),
    ]
