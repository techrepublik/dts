# Generated by Django 4.2.9 on 2024-01-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_office_office_branch_alter_department_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='office_name',
            field=models.CharField(max_length=50),
        ),
    ]
