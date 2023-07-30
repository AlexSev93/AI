from django.db import models


# Create your models here.
class Regions(models.Model):
    region = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.region


class Keywords(models.Model):
    word = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.word


class Vacancies(models.Model):
    vacancy = models.CharField(max_length=30)

    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    words = models.ManyToManyField(Keywords)

    def __str__(self):
        return f'{self.vacancy} в {self.regions}: {self.words.all()}'
