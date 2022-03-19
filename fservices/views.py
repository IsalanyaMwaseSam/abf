from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'fservices/main.html', {})

def gallery(request):
    return render(request, 'fservices/gallery.html', {})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = " " 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'eazikezi1999@gmail.com', ['eazikezi1999@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/home")
      
	form = ContactForm()
	return render(request, "fservices/contact.html", {'form':form})

def services(request):
	return render(request, "fservices/services.html", {})

def testimonies(request):
	return render(request, "fservices/testimonies.html", {})