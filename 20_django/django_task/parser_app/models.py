from django.db import models


# Create your models here.
class Regions(models.Model):
    region = models.CharField(max_length=30, unique=True)


class Keywords(models.Model):
    word = models.CharField(max_length=15, unique=True)


class Vacancies(models.Model):
    vacancy = models.CharField(max_length=30)
    region_name = models.CharField(max_length=30)

    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)


class Vacancies_Keywords(models.Model):
    vacancy = models.CharField(max_length=30)
    word = models.CharField(max_length=15)

    vacancies = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
    Keywords = models.ManyToManyField(Keywords)
