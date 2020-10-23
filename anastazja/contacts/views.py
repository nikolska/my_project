from django.shortcuts import render
from django.http import HttpResponse
from .models import Phone, Mail, Address

def search(request):
	tel = Phone.objects.all()
	email = Mail.objects.all()
	adrs = Address.objects.all()
	return render(request, 'contacts/contacts.html', {'tel':tel, 'email':email, 'adrs':adrs})
