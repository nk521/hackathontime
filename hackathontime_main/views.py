from django.shortcuts import render
from django.http import HttpResponse
from .models import Hackathon

def home(request):
	return render(request, 'hackathon/home.html')

# def about(request):
# 	return HttpResponse("<h1>about</h1>")