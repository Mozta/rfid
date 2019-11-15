from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import boto3

USERS_TABLE_NAME = os.environ['USERS_TABLE_NAME']
MACHINES_TABLE_NAME = os.environ['MACHINES_TABLE_NAME']

def home(request):
	return render(request, 'crud/home.html')

def user(request):

	if request.method == 'POST':
		dynamodb = boto3.resource('dynamodb')
		users_table = dynamodb.Table(USERS_TABLE_NAME)
		users_table.put_item(
			Item = {
			'authorized': True,
			'id': request.POST.get('id'),
			'name': request.POST.get('name'),
			})
		return redirect('crud-home')

	return render(request, 'crud/user.html')

def machine(request):

	if request.method == 'POST':
		dynamodb = boto3.resource('dynamodb')
		users_table = dynamodb.Table(MACHINES_TABLE_NAME)
		users_table.put_item(
			Item = {
			'description': request.POST.get('desc'),
			'id': request.POST.get('id'),
			'name': request.POST.get('name'),
			'available': True,
			'operator_id': ' '
			})
		return redirect('crud-home')

	return render(request, 'crud/machine.html')
