from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from colleges import *

class Hackathon(models.Model):
    hackathon_name = models.CharField(max_length=100)
    hackathon_content = models.TextField()
    hackathon_date_posted = models.DateTimeField(default=timezone.now)
    hackathon_date = models.DateTimeField()
    hackathon_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hackathon_name
