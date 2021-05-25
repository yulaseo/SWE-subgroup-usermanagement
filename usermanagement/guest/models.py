from django.db import models

# 다른 서브그룹이랑 맞춰야함
class Guest(models.Model):
    userid = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    password = models.TextField(default='')
    email = models.TextField(default='')
    phone_number = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    restricted_status = models.BooleanField(default=False)
    restricted_period = models.IntegerField(default=0)
