# Generated by Django 4.2.3 on 2023-08-01 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywords',
            name='word',
            field=models.CharField(max_length=15),
        ),
    ]