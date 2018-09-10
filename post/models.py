from django.db import models
from random import randint
import socket

# Create your models here.
class Posteo(models.Model):
    client_ip = socket.gethostname()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
