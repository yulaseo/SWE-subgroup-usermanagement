from django.db import models

class Feedback(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField()

class Reply(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()