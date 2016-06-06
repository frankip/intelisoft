from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from . models import Mail
# Create your views here.

def index(request):
	instance = Mail.objects.all()
	context = {
	'instance' : instance
	}
	return render (request, 'index.html')

def sendmail(request):
	subject, from_email, to = 'hello', 'fkipchumba@intellisoftplus.com', '[request.user.email]'
	text_content = 'hello!! you are reciving this because you are a privileged person '
	html_content = '<h2>Hello!!</h2> <br><p>you are receiving this because you are a <strong> privilged </strong> person.</p>'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	return render (request, 'index.html')