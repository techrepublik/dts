# Generated by Django 5.0.1 on 2024-01-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_office_office_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_website',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]