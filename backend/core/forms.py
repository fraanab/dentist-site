from django import forms
from .models import Appointment, Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ['date', 'time', 'message']
		widgets = {
			'message':forms.Textarea(attrs = {'Placeholder':'Message (optional)'}),
			'date':forms.DateTimeInput(attrs={'type':'date'}),
			'time':forms.TimeInput(attrs={'type':'time','min':'09:00','max':'17:00'})
		}
	# def __init__(self):
	# 	super().__init__()
	# 	for key, field in self.fields.items():
	# 		field.label = ""

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=50, required=True)
	last_name = forms.CharField(max_length=50, required=True)
	email = forms.EmailField(max_length=255, required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['email', 'message']
		widgets = {
			'email':forms.TextInput(attrs = {'Placeholder':'E-Mail'}),
			'message':forms.Textarea(attrs = {'Placeholder':'Message'})
		}