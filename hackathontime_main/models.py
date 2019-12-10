from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from hackathontime_users.models import Team
from django.utils.text import slugify
from colleges import *

class Hackathon(models.Model):
    hackathon_name = models.CharField(max_length=255)
    hackathon_content = models.TextField()
    hackathon_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hackathon_date = models.DateTimeField()
    hackathon_period = models.IntegerField(default=24)
    hackathon_points = models.FloatField(default=0.0, null=True)
    hackathon_future = models.BooleanField(default=True)
    hackathon_ongoing = models.BooleanField(default=False)
    hackathon_past = models.BooleanField(default=False)
    hackathon_date_posted = models.DateTimeField(default=timezone.now)
    hackathon_location_name = models.CharField(max_length=255, default="No venue as of now.")
    hackathon_location_url = models.URLField(max_length=255, default="null")
    hackathon_location_address = models.TextField(default="", blank=True)
    hackathon_team_going = models.ManyToManyField(Team, blank=True)
    hackathon_slug = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.hackathon_name

    def save(self, *args, **kwargs):
        self.hackathon_slug = slugify(self.hackathon_name)
        super(Hackathon, self).save(*args, **kwargs)
