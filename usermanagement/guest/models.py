from django.db import models

# 다른 서브그룹이랑 맞춰야함
class Guest(models.Model):
    userid = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.TextField()
    email = models.TextField()
    phone_number = models.IntegerField()
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    restricted_status = models.BooleanField(default=False)
    restricted_period = models.IntegerField(default=0)

class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    location = models.TextField()
    eBookAvailable = models.BooleanField(default=True)