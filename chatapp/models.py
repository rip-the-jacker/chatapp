from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    user = models.ForeignKey(User)
    message = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True)
