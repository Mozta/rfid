from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'crud/home.html')

def user(request):
	return render(request, 'crud/user.html')

def machine(request):
	return render(request, 'crud/machine.html')
