# Generated by Django 4.2.9 on 2024-01-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_office_office_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='agency',
            name='agency_website',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
