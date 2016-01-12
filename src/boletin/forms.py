from django import forms
from .models import Registrado



class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["email", "nombre", "media"]


	def clean_email(self):
		email = self.cleaned_data.get("email")
		
		email_base, proveedor = email.split("@")
		dominio, extension = proveedor.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Por favor utilice un email con la extension .edu")


		return email 


# class RegForm(forms.Form):
# 	nombre_form = forms.CharField(max_length=100)
# 	edad = forms.IntegerField()


