from django.db import models

# 다른 서브그룹이랑 맞춰야함
class Guest(models.Model):
    name = models.CharField(max_length=50)
    userid = models.IntegerField()
    password = models.TextField()
    email = models.TextField()
    phone_number = models.IntegerField()
    restricted_status = models.BooleanField(default=False)
    restricted_period = models.IntegerField(default=0)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)