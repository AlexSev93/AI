# Generated by Django 4.2.3 on 2023-07-30 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.CharField(max_length=30)),
                ('regions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserAPP.regions')),
                ('words', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserAPP.keywords')),
            ],
        ),
    ]
