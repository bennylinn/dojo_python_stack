from django.db import models
import datetime

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    duration = models.IntegerField()
    rating = models.IntegerField()
