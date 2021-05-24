from django.db import models

# 우리 서브그룹 내에서 맞추면 됨
class Feedback(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField()

class Reply(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()