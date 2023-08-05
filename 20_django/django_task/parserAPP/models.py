from django.db import models


# Create your models here.
class Regions(models.Model):
    region = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.region


class Keywords(models.Model):
    word = models.CharField(max_length=15)
    count = models.IntegerField()
    percent = models.FloatField(null=True)

    def __str__(self):
        return f'{self.word}:{self.count}<-->{self.percent}%'


class Vacancies(models.Model):
    vacancy = models.CharField(max_length=30)
    image = models.ImageField(upload_to='logo', null=True, blank=True)
    regions = models.CharField(max_length=30)
    words = models.ManyToManyField(Keywords)

    def __str__(self):
        return f'{self.vacancy}>{self.regions}: {[str(w) for w in self.words.all()]}'
