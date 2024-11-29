# Generated by Django 5.1.3 on 2024-11-29 20:05

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0069_alter_note_audio_alter_note_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={},
        ),
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='guidancecategory',
            options={},
        ),
        migrations.AlterModelOptions(
            name='guidancepost',
            options={'ordering': ['rank']},
        ),
        migrations.AlterModelOptions(
            name='guide',
            options={},
        ),
        migrations.AlterModelOptions(
            name='hajsteps',
            options={'ordering': ['rank']},
        ),
        migrations.AlterModelOptions(
            name='management',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={},
        ),
        migrations.AlterModelOptions(
            name='pilgrim',
            options={},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={},
        ),
        migrations.AlterModelOptions(
            name='religiouscategory',
            options={},
        ),
        migrations.AlterModelOptions(
            name='religiouspost',
            options={'ordering': ['rank']},
        ),
        migrations.AlterModelOptions(
            name='secondarysteps',
            options={},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterModelOptions(
            name='usernotification',
            options={},
        ),
        migrations.AlterModelOptions(
            name='verificationcode',
            options={},
        ),
        migrations.AlterField(
            model_name='basenotification',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='basenotification',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='basenotification',
            name='info',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='basenotification',
            name='sentBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='basenotification',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.chat'),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='content',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='sent_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='get_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='images/account.jpg', upload_to='images/users'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(db_index=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{5,15}$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='guidancecategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='guidancecategory',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guidancepost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.guidancecategory'),
        ),
        migrations.AlterField(
            model_name='guidancepost',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='guidancepost',
            name='cover',
            field=models.ImageField(upload_to='cover'),
        ),
        migrations.AlterField(
            model_name='guidancepost',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='guidancepost',
            name='rank',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='guidancepost',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hajsteps',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hajsteps',
            name='note',
            field=models.CharField(default='note', max_length=500),
        ),
        migrations.AlterField(
            model_name='hajsteps',
            name='rank',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='hajsteps',
            name='secondary_steps',
            field=models.ManyToManyField(to='base.secondarysteps'),
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.guide'),
        ),
        migrations.AlterField(
            model_name='note',
            name='pilgrim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.pilgrim'),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='arrival',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='boarding_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='company_logo',
            field=models.ImageField(blank=True, default='images/account.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='departure',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='duration',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='father_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='flight_company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='flight_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='flight_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='from_city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='gate_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='grand_father',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.guide'),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='haj_steps',
            field=models.ManyToManyField(blank=True, through='base.HaJStepsPilgrim', to='base.hajsteps'),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='hotel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='hotel_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='phonenumber',
            field=models.CharField(db_index=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{5,15}$')]),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='registeration_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='room_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='to_city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registration',
            name='address',
            field=models.CharField(choices=[('القديح', 'القديح'), ('القطيف', 'القطيف'), ('صفوى', 'صفوى'), ('سيهات', 'سيهات'), ('العوامية', 'العوامية'), ('الجارودية', 'الجارودية'), ('الجش', 'الجش'), ('الأوجام', 'الأوجام'), ('تاروت', 'تاروت'), ('أخرى', 'أخرى')], max_length=15),
        ),
        migrations.AlterField(
            model_name='registration',
            name='alhajj',
            field=models.CharField(blank=True, choices=[('حج واجب  ( أحج لأول مرة )', 'حج واجب  ( أحج لأول مرة )'), ('حج مستحب ( حججت مسبقا )', 'حج مستحب ( حججت مسبقا )'), ('حج نيابي ( أحج نيابة عن غير )', 'حج نيابي ( أحج نيابة عن غير )'), ('تاروت', 'تاروت'), ('عما في الذمة ( أحج لبراءة ذمتي )', 'عما في الذمة ( أحج لبراءة ذمتي )')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='count_hajjas',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='father_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('ذكر', 'ذكر'), ('أنثى', 'أنثى')], max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='grand_father',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='id_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='illness',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='job_position',
            field=models.CharField(blank=True, choices=[('موظف حكومي', 'موظف حكومي'), ('موظف شركة', 'موظف شركة'), ('موظف أهلي', 'موظف أهلي'), ('طالب', 'طالب'), ('مهندس', 'مهندس'), ('طبيب', 'طبيب'), ('معلم', 'معلم'), ('طالب علم', 'طالب علم'), ('ممرض', 'ممرض'), ('ربة بيت', 'ربة بيت'), ('متسيب', 'متسيب'), ('تاجر', 'تاجر'), ('غير ذلك', 'غير ذلك')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='last_year',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='marital_status',
            field=models.CharField(choices=[('متزوج', 'متزوج'), ('أعزب', 'أعزب'), ('مطلق', 'مطلق')], max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='means_journey',
            field=models.CharField(choices=[('طيران ذهاب وعودة', 'طيران ذهاب وعودة'), ('ذهاب (طيران) والعودة (حافلة)', 'ذهاب (طيران) والعودة (حافلة)'), ('ذهاب (حافلة) والعودة (طيران)', 'ذهاب (حافلة) والعودة (طيران)'), ('حافلة ذهاب وعودة', 'حافلة ذهاب وعودة')], max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='options_trip',
            field=models.CharField(choices=[('المدينة و مكة', 'المدينة و مكة'), ('مكة فقط', 'مكة فقط')], max_length=20),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phonenumber',
            field=models.CharField(unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{5,15}$')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='sai',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='tawaf',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='tradition_reference',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='type_help',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='wheelchair',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='religiouscategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='religiouscategory',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='religiouspost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.religiouscategory'),
        ),
        migrations.AlterField(
            model_name='religiouspost',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='religiouspost',
            name='cover',
            field=models.ImageField(upload_to='cover'),
        ),
        migrations.AlterField(
            model_name='religiouspost',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='religiouspost',
            name='rank',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='religiouspost',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='secondarysteps',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='secondarysteps',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='secondarysteps',
            name='note',
            field=models.CharField(default='note', max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='phonenumber',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
