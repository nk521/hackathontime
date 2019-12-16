from django.contrib import admin
from .models import Profile, Team, Comment #, Post

admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Comment)
# admin.site.register(Post)
# Register your models here.
