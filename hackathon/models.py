from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Hackathon_Submit(models.Model):
	hackathon_name = models.CharField(max_length=100)
	hackathon_content = models.TextField()
	hackathon_date_posted = models.DateTimeField(default=timezone.now)
	hackathon_date = models.DateTimeField()
	hackathon_author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.hackathon_name