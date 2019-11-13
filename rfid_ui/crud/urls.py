from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='crud-home'),
	path('user', views.user, name='crud-user'),
	path('machine', views.machine, name='crud-machine')
]