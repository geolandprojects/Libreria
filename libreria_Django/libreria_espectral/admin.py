# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Taxon, Evento, Firma_Espectral, Ubicacion

# Register your models here.

admin.site.register(Taxon)
admin.site.register(Evento)
admin.site.register(Firma_Espectral)
admin.site.register(Ubicacion)