from django.db import models
from django.contrib.auth.models import User

class User_films(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Genere(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    director = models.CharField(max_length=200, null=True)
    generes = models.ManyToManyField(Genere)
    users = models.ManyToManyField(User)
    def __str__(self):
        return self.title
