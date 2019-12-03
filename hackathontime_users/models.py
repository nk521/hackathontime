# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from colleges import *

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_college = models.CharField(max_length=200, choices=colleges_list, blank=True)
#     user_bio = models.TextField(max_length=500, blank=True)
#     user_state = models.CharField(max_length=30, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
