from django.db import models


class IndiaNews(models.Model):
    data = models.CharField(max_length=100)


class WorldNews(models.Model):
    data = models.CharField(max_length=100) 


class BusinessNews(models.Model):
    data = models.CharField(max_length=100)


class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    imdb = models.DecimalField(max_digits=5, decimal_places=2)
    metascores = models.IntegerField(null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)
