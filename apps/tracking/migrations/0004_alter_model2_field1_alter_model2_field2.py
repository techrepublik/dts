# Generated by Django 5.0.1 on 2024-02-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_model1_model2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model2',
            name='field1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='model2',
            name='field2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
