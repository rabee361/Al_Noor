# Generated by Django 5.1.3 on 2024-12-25 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0070_alter_chat_options_alter_chatmessage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio/pilgrims', verbose_name='الملف الصوتي'),
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='الملاحظات'),
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='التاريخ'),
        ),
        migrations.AlterField(
            model_name='note',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.guide', verbose_name='المرشد'),
        ),
        migrations.AlterField(
            model_name='note',
            name='pilgrim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.pilgrim', verbose_name='الحاج'),
        ),
    ]
