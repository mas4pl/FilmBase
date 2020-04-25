from django.db import models

# Create your models here.
class Movie(models.Model):
    nr = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    #director = models.CharField(max_length=200)
    year = models.DateField()
    gener = models.CharField(max_length=100)
