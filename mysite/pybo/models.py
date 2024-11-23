from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    ip_address = models.CharField(max_length=20, null=True) 
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return f"{self.subject}, {self.content}, {self.create_date}"

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    ip_address = models.CharField(max_length=20, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField()
