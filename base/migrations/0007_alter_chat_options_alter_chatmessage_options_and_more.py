# Generated by Django 5.0.4 on 2024-04-15 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_pilgrim_arrival_alter_pilgrim_birthday_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'محادثة', 'verbose_name_plural': 'محادثات'},
        ),
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['-timestamp'], 'verbose_name': 'رسالة', 'verbose_name_plural': 'رسائل'},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-id'], 'verbose_name': 'مستخدم', 'verbose_name_plural': 'مستخدمين'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-id'], 'verbose_name': 'موظف', 'verbose_name_plural': 'موظفين'},
        ),
        migrations.AlterModelOptions(
            name='guidancecategory',
            options={'verbose_name': 'نوع الارشاد', 'verbose_name_plural': 'أنواع الارشاد الديني'},
        ),
        migrations.AlterModelOptions(
            name='guidancepost',
            options={'ordering': ['-created'], 'verbose_name': 'إرشاد ديني', 'verbose_name_plural': 'إرشادات دينية'},
        ),
        migrations.AlterModelOptions(
            name='guide',
            options={'verbose_name': 'المرشد', 'verbose_name_plural': 'المرشدين'},
        ),
        migrations.AlterModelOptions(
            name='management',
            options={'ordering': ['-id'], 'verbose_name': 'مدير', 'verbose_name_plural': 'الادارة'},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'ملاحظة', 'verbose_name_plural': 'ملاحظات'},
        ),
        migrations.AlterModelOptions(
            name='pilgrim',
            options={'verbose_name': 'حاج', 'verbose_name_plural': 'الحجاج'},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'verbose_name': 'الحاج', 'verbose_name_plural': 'الحجاج'},
        ),
        migrations.AlterModelOptions(
            name='religiouscategory',
            options={'verbose_name': 'نوع عمل ديني', 'verbose_name_plural': 'أنواع العمل الديني'},
        ),
        migrations.AlterModelOptions(
            name='religiouspost',
            options={'ordering': ['-created'], 'verbose_name': 'عمل ديني', 'verbose_name_plural': 'أعمال دينية'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'مهمة', 'verbose_name_plural': 'مهام'},
        ),
        migrations.AlterModelOptions(
            name='usernotification',
            options={'verbose_name': 'اشعار', 'verbose_name_plural': 'اشعارات'},
        ),
        migrations.AlterModelOptions(
            name='verificationcode',
            options={'verbose_name': 'رمز التأكيد', 'verbose_name_plural': 'رموز التأكيد'},
        ),
    ]
