# Generated by Django 5.0.1 on 2024-01-24 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_alter_document_category_id_alter_document_flow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='office_user',
        ),
    ]