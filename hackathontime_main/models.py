from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Profile(models.Model):
# 	"""
# 	state = (
# 		()
# 	)
# 	"""
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_college = models.CharField(max_length=30)
#     user_bio = models.TextField(max_length=500, blank=True)
#     user_state = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# class Team(models.Model):
# 	Team_name = models.CharField(max_length=20)
# 	Team_bio = models.TextField(max_length=500)
# 	Team_captain = models.

class Hackathon(models.Model):
	hackathon_name = models.CharField(max_length=100)
	hackathon_content = models.TextField()
	hackathon_date_posted = models.DateTimeField(default=timezone.now)
	hackathon_date = models.DateTimeField()
	hackathon_author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.hackathon_name
