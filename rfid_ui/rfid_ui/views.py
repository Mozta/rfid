from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('''
		<a href="logs">logs</a>
		<br>
		<a href="register">register</a>
		''')