from django.urls import path
from .views import frontpage, newAppointment, bookpage, signup, success, myaccount, delete, update, contact, admin, deletemsg
from django.contrib.auth import views

urlpatterns = [
	path('', frontpage, name="frontpage"),
	path('contact/', contact, name='contact'),
	path('newAppointment/', newAppointment, name="newAppointment"),
	path('booking/', bookpage, name='bookpage'),
	path('success/', success, name="success"),
	path('signup/', signup, name='signup'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
	path('myaccount/', myaccount, name='myaccount'),
	path('dashboard/', admin, name='dashboard'),
	path('delete/<int:pk>/', delete, name='delete'),
	path('deletemsg/<int:pk>/', deletemsg, name='deletemsg'),
	path('update/<int:pk>/', update, name='update'),
]