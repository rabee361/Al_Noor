# Generated by Django 5.0.4 on 2024-04-16 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_chat_options_alter_chatmessage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HajSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('additional_info', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StepType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pilgrim',
            name='haj_steps',
            field=models.ManyToManyField(blank=True, to='base.hajsteps'),
        ),
        migrations.AddField(
            model_name='hajsteps',
            name='step_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.steptype'),
        ),
    ]
