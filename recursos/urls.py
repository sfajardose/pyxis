from django.conf.urls import url

from recursos.views import (
    PersonalProyecto,
    ProduccionPersona,
    ProduccionProyecto,
    ProyectoTipo
)

urlpatterns = [
    url(
        r'proyecto-personal/$',
        PersonalProyecto.as_view(),
        name='proyecto-personal'
    ),
    url(
        r'proyecto-tipo/$',
        ProyectoTipo.as_view(),
        name='proyecto-tipo'
    ),
    url(
        r'produccion-persona/$',
        ProduccionPersona.as_view(),
        name='produccion-persona'
    ),
    url(
        r'produccion-proyecto/$',
        ProduccionProyecto.as_view(),
        name='produccion-proyecto'
    ),
]
