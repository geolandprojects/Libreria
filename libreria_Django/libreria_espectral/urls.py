from django.conf.urls import include, url
from . import views #Le decimos a Django que de este directorio importe el fichero views

urlpatterns = [
    url( r'^$' , views.primer_vista, name= 'primera-vista' ),
	url( r'^eventos/$', views.eventos, name='all-eventos'), #nueva url
	url(r'^eventos/(\d+)/$', views.detail_evento, name='detail-evento'),#url para detalles
]