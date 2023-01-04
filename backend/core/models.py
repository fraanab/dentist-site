from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=255)
	message = models.TextField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)

class Contact(models.Model):
	email = models.EmailField(max_length=255)
	message = models.TextField(max_length=255)
	sent_at = models.DateTimeField(auto_now_add=True)