from django.contrib import admin
from .models import Appointment, Contact


class BookAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'message', 'date', 'time','created_at')
	list_filter = ('date','time',)
	search_fields = ['email', 'message', 'first_name', 'last_name']
class ContactAdmin(admin.ModelAdmin):
	list_display=('email','message','sent_at')
	list_filter=('sent_at',)
	search_fields=['email','message']

admin.site.register(Appointment, BookAdmin)
admin.site.register(Contact, ContactAdmin)