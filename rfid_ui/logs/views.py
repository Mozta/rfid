from django.shortcuts import render
import os
import boto3
from pprint import pprint as pp
from datetime import datetime

LOGS_TABLE_NAME = os.environ['LOGS_TABLE_NAME']
USERS_TABLE_NAME = os.environ['USERS_TABLE_NAME']
MACHINES_TABLE_NAME = os.environ['MACHINES_TABLE_NAME']

# known_users = []
# known_machines = []

dynamodb = boto3.resource('dynamodb')

def process_scan_results(item):

	machine_id = item['machine_id']
	user_id = item['user_id']

	# Get user's name from id
	users_table = dynamodb.Table(USERS_TABLE_NAME)
	user_name = users_table.query(
		KeyConditionExpression = 'id = :id',
		ExpressionAttributeValues = {
			':id': item['user_id']
		},
		Select = 'SPECIFIC_ATTRIBUTES',
		ProjectionExpression = '#name',
		ExpressionAttributeNames = {
			'#name': 'name'
		}
	)['Items'][0]

	# Get machine's name from id
	machines_table = dynamodb.Table(MACHINES_TABLE_NAME)
	machine_name = machines_table.query(
		KeyConditionExpression = 'id = :id',
		ExpressionAttributeValues = {
			':id': item['machine_id']
		},
		Select = 'SPECIFIC_ATTRIBUTES',
		ProjectionExpression = '#name',
		ExpressionAttributeNames = {
			'#name': 'name'
		}
	)['Items'][0]

	# check if activity has not finished
	if 'end_timestamp' in item:
		endtime = datetime.fromtimestamp(item['end_timestamp'])
	else:
		endtime = None

	# Create output object
	return {
		'machine': str(f'{machine_name} (id: {machine_id})'),
		'start': datetime.fromtimestamp(item['start_timestamp']),
		'end': endtime,
		'user': str(f'{user_name} (id: {user_id})')
	}

def home(request):

	# Get logs from db and process them
	logs_table = dynamodb.Table(LOGS_TABLE_NAME)
	logs = logs_table.scan(
		Limit = 20,
	)['Items']
	logs = list(map(process_scan_results, logs))


	pp(logs)

	return render(request, 'logs/home.html', context={'logs': logs})