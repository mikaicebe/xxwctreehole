from django.db import models


# Create your models here.
class Message(models.Model):
    message_text = models.TextField()
    time = models.DateTimeField()


class Comment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    comment_text = models.TextField()
    time = models.DateTimeField()
