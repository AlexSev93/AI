# Generated by Django 4.2.3 on 2023-08-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPP', '0010_alter_vacancies_regions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancies',
            name='regions',
            field=models.CharField(max_length=30),
        ),
    ]
