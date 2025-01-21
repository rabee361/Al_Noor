# Generated by Django 5.1.3 on 2025-01-21 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0075_registration_additional'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.TextField(verbose_name='الأحكام و الشروط')),
                ('privacy', models.TextField(verbose_name='سياسة الخصوصية')),
            ],
        ),
        migrations.AlterField(
            model_name='registration',
            name='additional',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='اسم المرافق معك'),
        ),
    ]
