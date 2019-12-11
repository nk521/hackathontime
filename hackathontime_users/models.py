# from django.db import models
# from django.utils import timezone

from colleges import *
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify

class Team(models.Model):
	team_name = models.CharField(max_length=20,unique=True)
	team_points = models.FloatField(default=0.0)
	team_slug = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return f'{self.team_name}'

	def save(self, *args, **kwargs):
		if not self.team_slug:
			self.team_slug = slugify(self.team_name)
		super(Team, self).save(*args, **kwargs)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	gender = models.CharField(max_length=1, choices=[('F', 'Female'),('M', 'Male'),("O", "Others"),("X", "Prefer not to say")], blank=True, null=True)
	college = models.CharField(max_length=255, choices=colleges_list, blank=True, null=True) #3739 is choose college
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)
	is_in_a_team = models.BooleanField(default=False)
	bio = models.TextField(max_length=500, null=True, blank=True)
	slug = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return f'{self.user.username}'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.user.username)
		if not self.bio:
			self.bio = "*No bio*"
		super(Profile, self).save(*args, **kwargs)
		
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			min_side = min(img.height, img.width)
			if min_side == img.height:
			# https://opensource.com/life/15/2/resize-images-python
				height = 300
				hpercent = (height / float(img.size[1]))
				width = int((float(img.size[0]) * float(hpercent)))
				img.thumbnail((width, height))
				img.save(self.image.path)

			elif min_side == img.width:
				width = 300
				wpercent = (width / float(img.size[1]))
				height = int((float(img.size[0]) * float(wpercent)))
				img.thumbnail((width, height))
				img.save(self.image.path)

			else:
				img.thumbnail((300,300))
				img.save(self.image.path)
