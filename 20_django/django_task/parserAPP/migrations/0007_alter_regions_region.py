# Generated by Django 4.2.3 on 2023-08-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPP', '0006_alter_regions_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions',
            name='region',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]