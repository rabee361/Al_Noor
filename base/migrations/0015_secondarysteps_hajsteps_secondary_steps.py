# Generated by Django 5.0.4 on 2024-04-24 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_registration_options_usernotification_info_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondarySteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='hajsteps',
            name='secondary_steps',
            field=models.ManyToManyField(to='base.secondarysteps'),
        ),
    ]