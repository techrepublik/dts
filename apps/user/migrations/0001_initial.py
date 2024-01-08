# Generated by Django 4.1.12 on 2024-01-07 16:28

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('middle_name', models.CharField(blank=True, max_length=20)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('office_user', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(max_length=50)),
                ('ageny_address', models.CharField(max_length=50)),
                ('agency_head', models.CharField(max_length=50)),
                ('agency_contact', models.CharField(max_length=50)),
                ('agency_email', models.CharField(max_length=50)),
                ('agency_website', models.CharField(max_length=50)),
                ('agency_logo1', models.ImageField(blank=True, null=True, upload_to='static/dist/img/agency_logo')),
                ('agency_logo2', models.ImageField(blank=True, null=True, upload_to='static/dist/img/agency_logo')),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(blank=True, max_length=50, null=True)),
                ('office_head', models.CharField(max_length=50)),
                ('office_description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='office_agency_name', to='user.agency')),
            ],
        ),
        migrations.CreateModel(
            name='Office_User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_office_name', to='user.office')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='office_user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Office_User',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
            managers=[
                ('personel', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
