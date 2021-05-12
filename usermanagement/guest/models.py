from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=50)
    userid = models.IntegerField()
    restricted_status = models.BooleanField(default=False)
    restricted_period = models.IntegerField(default=0)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)