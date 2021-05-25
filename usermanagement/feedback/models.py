from django.db import models

# 우리 서브그룹 내에서 맞추면 됨
class Feedback(models.Model):
    feedbackid = models.IntegerField(null=False, primary_key=True)
    anonimity = models.TextField()
    userid = models.TextField(null=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()