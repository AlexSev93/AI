# Generated by Django 4.2.3 on 2023-08-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPP', '0005_keywords_percent_alter_vacancies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions',
            name='region',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
