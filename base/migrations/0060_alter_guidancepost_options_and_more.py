# Generated by Django 5.0.4 on 2024-06-07 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0059_alter_guidancepost_rank_alter_hajsteps_rank_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guidancepost',
            options={'ordering': ['rank'], 'verbose_name': 'إرشاد ديني', 'verbose_name_plural': 'إرشادات دينية'},
        ),
        migrations.AlterModelOptions(
            name='religiouspost',
            options={'ordering': ['rank'], 'verbose_name': 'عمل ديني', 'verbose_name_plural': 'أعمال دينية'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(db_index=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{5,15}$')], verbose_name='رقم الهاتف'),
        ),
    ]