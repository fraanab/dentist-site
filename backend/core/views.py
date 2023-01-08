from django.shortcuts import render, redirect
from .forms import AppointmentForm, SignUpForm, ContactForm
from .models import Appointment, Contact
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from datetime import timedelta
from django.http import HttpResponse
from django.core.mail import send_mail #newsletter
from django.template.loader import render_to_string
from django.conf import settings

def frontpage(request):
	appointmentForm = AppointmentForm()

	context = {
		'appointmentForm':appointmentForm
	}
	return render(request, 'frontpage.html', context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})

@login_required
def newAppointment(request):
	if request.method == 'POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			formpause = form.save(commit=False)
			formpause.username = request.user
			if Appointment.objects.filter(date=formpause.date).count() >=1:
				formpause.date += timedelta(days=1)
			formpause.save()
			Appointment.objects.filter(date=formpause.date).update(first_name=request.user.first_name, last_name=request.user.last_name, email=request.user.email)
			print('Appointment booked. Date: ', formpause.date)
			return redirect('success')
		else:
			print('Appointment failed')
			return redirect('/')

def success(request):
	return render(request, 'success.html')

def myaccount(request):
	userappointment = Appointment.objects.filter(username=request.user)
	if request.user.is_superuser:
		return redirect('dashboard')
	if request.method == 'POST':
		userappointment.delete()
		return redirect('myaccount')
	return render(request, 'myaccount.html', {'userappointment':userappointment})

def delete(request, pk):
	appointment = Appointment.objects.filter(pk=pk)
	if request.method == 'POST':
		appointment.delete()
		return redirect('myaccount')

def deletemsg(request, pk):
	message = Contact.objects.filter(pk=pk)
	if request.method == 'POST':
		message.delete()
		return redirect('dashboard')

@login_required
def update(request, pk):
	appointment = Appointment.objects.get(pk=pk)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		message = request.POST.get('message')
		date = request.POST.get('date')
		time = request.POST.get('time')
		Appointment.objects.filter(pk=pk).update(first_name=first_name, last_name=last_name, message=message, date=date, time=time)

		subject = 'Your appointment has been updated'
		body = render_to_string('updatemail.html', {'appointment':appointment})
		plain_message = f'Mr/Mrs {last_name}, Your new appointment date is: {date} at {time}. If this is not correct, visit the website now, or try to reach us a call. Thank you.'
		
		send_mail(
				f'{subject}',
				f'{plain_message}',
				settings.EMAIL_HOST_USER,
				[f'{appointment.email}'],
				html_message=body,
				fail_silently=False,
			)
		return redirect('myaccount')
	return render(request, 'update.html', {'appointment':appointment})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ContactForm()

	return render(request, 'contact.html', {'form':form})

@login_required
def admin(request):
	if request.user.is_superuser:
		appointments = Appointment.objects.all()
		contact_messages = Contact.objects.all()

		contact_total = contact_messages.count()
		appointments_total = appointments.count()
		context = {
			'appointments':appointments,
			'appointments_total':appointments_total,

			'contact_messages':contact_messages,
			'contact_total':contact_total
		}
		return render(request, 'dashboard.html', context)
	else:
		redirect('/')

def bookpage(request):
	appointmentForm = AppointmentForm()

	context = {
		'appointmentForm':appointmentForm
	}
	return render(request, 'booking.html', context)