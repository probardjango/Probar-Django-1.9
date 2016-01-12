from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registrado(models.Model):
	nombre = models.CharField(max_length=120, blank=True, null=True)
	email = models.EmailField()
	codigo_postal = models.IntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)
	media = models.FileField(upload_to='myfolder/', blank=True, null=True) #barra despues NO antes


	def __unicode__(self): #Python 3 __str__
		return self.email