from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mail(models.Model):
	subject = models.CharField(max_length=140)
	e_mail = models.EmailField()
	
	def __unicode__(self):
		return self.subject

	def __str__(self):
		return self.subject

		