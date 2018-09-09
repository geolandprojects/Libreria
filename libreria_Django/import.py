import csv,sys,os

project_dir = 'C:\Users\User\Desktop\virtual-biblioteca\libreria\libreria'

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django
django.setup[]

from libreria_espectral.models import Firma_Espectral