from django.db import models

# Create your models here.
class Movie(models.Model):
    #nr = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    director = models.CharField(max_length=200)
    gener = models.CharField(max_length=100)
