# Generated by Django 5.0.1 on 2024-01-24 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_remove_tracking_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking',
            name='status',
        ),
    ]
