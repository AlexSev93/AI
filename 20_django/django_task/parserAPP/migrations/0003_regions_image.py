# Generated by Django 4.2.3 on 2023-08-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPP', '0002_alter_keywords_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='regions',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='regions'),
        ),
    ]