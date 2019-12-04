# from django.db import models
# from django.utils import timezone
# from colleges import *

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username}\'s profile'

	def save(self):
		super().save()
		
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


# class Team(model.Model):