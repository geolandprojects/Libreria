# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Creación de modelos.

#____________________________________________________________________
class Taxon(models.Model):
	nombre_cientifico = models.CharField(max_length=200)
	reino = models.CharField(max_length=200)
	filo = models.CharField(max_length=200)
	clase = models.CharField(max_length=200)
	orden = models.CharField(max_length=200)
	familia = models.CharField(max_length=200)
	genero = models.CharField(max_length=200)
	epiteto_especifico = models.CharField(max_length=200)
	autoria_nombre_cientifico = models.CharField(max_length=200)
		
	def __unicode__(self):#__str__ para python 3
		return self.nombre_cientifico
		
	class Meta:
		verbose_name_plural = 'Taxon'

#____________________________________________________________________
class Evento(models.Model):
	fecha_captura = models.DateField()
	hora_captura = models.TimeField()
	estado_desarrollo = models.CharField(max_length=45)
	altura_individuo = models.CharField(max_length=45)
	altura_instrumental = models.CharField(max_length=45)
	estado_tiempo = models.CharField(max_length=45)
	imagen_individuo = models.ImageField(upload_to = 'media/individuo/')#Crea una carpeta llamada individuo, donde guardara las imagenes los individuos, al final la imagen tendra que cargarse en: media/individuo/
	imagen_cielo = models.ImageField(upload_to = 'media/cielo/')
	imagen_panorama = models.ImageField(upload_to = 'media/panorama/')
	taxon = models.ForeignKey(Taxon)
	
	def __unicode__(self):#__str__ para python 3
		cadena = "%s - %s - %s - %s" %(self.taxon,self.estado_desarrollo,self.estado_tiempo, self.fecha_captura)
		return cadena
		
	class Meta:
		verbose_name_plural = 'Evento'
#____________________________________________________________________
class Firma_Espectral(models.Model):
	longitud_onda = models.IntegerField(default=0)
	firma = models.DecimalField(max_digits=18, decimal_places=16)
	evento=models.OneToOneField(Evento,null=True, blank=True, on_delete=models.CASCADE)
	#taxon = models.ForeignKey(Taxon)
	
	class Meta:
		verbose_name_plural = 'Firma Espectral'
#____________________________________________________________________
class Ubicacion(models.Model):
	pais = models.CharField(max_length=45)
	codigo_pais = models.CharField(max_length=45)
	departamento = models.CharField(max_length=45)
	municipio = models.CharField(max_length=45)
	localidad = models.CharField(max_length=45)
	elevacion = models.FloatField()
	comentario_ubicacion = models.CharField(max_length=200)
	codigo_pais = models.CharField(max_length=45)
	latitud = models.DecimalField(max_digits=9, decimal_places=6)
	longitud = models.DecimalField(max_digits=9, decimal_places=6)
	evento=models.OneToOneField(Evento,null=True, blank=True, on_delete=models.CASCADE)
	#taxon = models.ForeignKey(Taxon)
	
	def __unicode__(self):#__str__ para python 3
		cadena2 = "%s - %s - %s - %s - %s" %(self.departamento,self.municipio,self.localidad, self.elevacion, self.evento)
		return cadena2
		
	class Meta:
		verbose_name_plural = 'Ubicación'
	
	
	
