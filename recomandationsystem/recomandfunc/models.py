from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Movie(models.Model):
    movieId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)

class Rating(models.Model):
    userId = models.IntegerField()
    movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    timestamp = models.IntegerField()
