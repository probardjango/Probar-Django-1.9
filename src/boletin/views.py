from django.shortcuts import render
from .forms import RegistradoForm
from .models import Registrado

# Create your views here.



def inicio(request):	
	titulo = "Bienvenidos"
	form = RegistradoForm(request.POST or None, request.FILES or None)
	queryset = Registrado.objects.all()

	for obj in queryset:
		print obj.nombre
		# print obj.email
		# print obj.id
	
	context = {
		"titulo": titulo,
		"form": form,
		"queryset": queryset
	}


	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		form.save()

		context = {
			"titulo": "Gracias %s, ya se ha registrado." %(nombre)
		}
		if not nombre:
			context = {
				"titulo": "Gracias %s, ya se ha registrado." %(email)
			}
		# print instance.email
		# print instance.timestamp
	# if request.user.is_authenticated():
	# titulo = "Hola, %s!" %(request.user)	


	return render(request, "inicio.html", context)


	
def sobre(request):	
	titulo = "Sobre Nosotros"
	
	context = {
		"titulo": titulo,
	}

	return render(request, "sobre.html", context)


