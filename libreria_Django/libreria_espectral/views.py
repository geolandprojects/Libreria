# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Taxon, Evento, Firma_Espectral, Ubicacion #Importamos los modelos

# Create your views here.

def primer_vista(request):#siempre recibe un parametro HttpRequest
	return HttpResponse("Hola, soy tu primera vista")
	
def eventos(request):
	# Esta vista se encarga de hacer las gestiones para mostrar todos los libros de la BD en allbooks.html

	all_eventos = Evento.objects.all() #traemos todos los libros
	context = {'object_list':all_eventos}
	return render(request, 'libreria_espectral/alleventos.html', context) #retornamos un HttpResponse
	
def detail_evento(request, id_evento):
	evento = Evento.objects.get(id=id_evento)
	context = {'object':evento}
	return render(request, 'libreria_espectral/detailevento.html', context)