# Generated by Django 4.1.12 on 2024-01-08 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_office_user_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]