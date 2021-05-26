from django.db import models
from django.contrib.auth.models import AbstractUser

class Guest(AbstractUser):
    userid = models.IntegerField(null=True, default="9999999999")
    # name = models.CharField(max_length=50, null=False)
    # password = models.TextField(default='')
    # email = models.TextField(default='')
    phone_number = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    restricted_status = models.BooleanField(default=False)
    restricted_period = models.IntegerField(default=0)

    def __str__(self):
        return self.username
