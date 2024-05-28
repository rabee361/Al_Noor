# Generated by Django 5.0.4 on 2024-05-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_alter_pilgrim_guide_alter_registration_options_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='الاسم')),
                ('phonenumber', models.CharField(max_length=100, verbose_name='رقم الهاتف')),
                ('password', models.CharField(max_length=100, verbose_name='كلمة السر')),
            ],
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='haj_steps',
            field=models.ManyToManyField(blank=True, to='base.hajsteps', verbose_name='خطوات الحملة'),
        ),
    ]
