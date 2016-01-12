from django.contrib import admin

# Register your models here.
from .forms import RegistradoForm
from .models import Registrado 


class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__unicode__", "nombre", "codigo_postal", "timestamp", "actualizado"]
	form = RegistradoForm
	# class Meta:
	# 	model = Registrado


admin.site.register(Registrado, AdminRegistrado)