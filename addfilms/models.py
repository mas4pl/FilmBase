from django.db import models

class Genere(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# Create your models here.
class Movie(models.Model):
    #nr = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    director = models.CharField(max_length=200, null=True)
    generes = models.ManyToManyField(Genere)
    def __str__(self):
        return self.title
