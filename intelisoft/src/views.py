from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from . models import Mail
# Create your views here.

def index(request):
	instance = Mail.objects.all()

	to = 'p@.com'
	subject = ""
	message= ""

	# send(to,subject,message)

	context = {
	'instance' : instance
	}
	return render (request, 'index.html', context)

def sendmail(request):
	subject = 'hello'
	to = 'gwadafrank@gmail.com'
	message= 'This is an important message.'

	send(subject,to, message)

	return render (request, 'index.html')



def send(subject,to, message):
	subject, to, message, from_email = subject, to , message, 'franciskipchumba5@gmail.com'
	html_content = '<p>This is an <strong>important</strong> message.</p>'
	msg = EmailMultiAlternatives(subject, message, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return 