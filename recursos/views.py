from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from recursos.models import (
    Documento,
    Produccion,
    Proyecto,
    UsuarioProyecto,
    Usuario
)


class PersonalProyecto(LoginRequiredMixin, TemplateView):
    template_name = 'recursos/personal-proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(PersonalProyecto, self).get_context_data(**kwargs)
        proyectos = Proyecto.objects.all()

        proyecto_usuarios = list()
        for proyecto in proyectos:
            proyectos = UsuarioProyecto.objects.filter(proyecto=proyecto)
            proyecto_usuarios.append(
                {
                    'proyecto': proyecto.nombre,
                    'usuarios': len(proyectos)
                }
            )

        context['proyecto_usuarios'] = proyecto_usuarios
        return context


class ProyectoTipo(LoginRequiredMixin, TemplateView):
    template_name = 'recursos/proyecto-tipo.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoTipo, self).get_context_data(**kwargs)
        tipos_proyecto = Proyecto.objects.values('tipo').annotate(
            proyectos=Count('tipo')
        )

        context['tipos_proyecto'] = tipos_proyecto
        return context


class ProduccionPersona(LoginRequiredMixin, TemplateView):
    template_name = 'recursos/produccion-persona.html'

    def get_context_data(self, **kwargs):
        context = super(ProduccionPersona, self).get_context_data(**kwargs)
        personas = Usuario.objects.all()

        produccion_persona = list()
        for persona in personas:
            personas = Produccion.objects.filter(usuario=persona)
            produccion_persona.append(
                {
                    'persona': persona.primer_nombre + ' ' +
                    persona.primer_apellido,
                    'documentos': len(personas)
                }
            )

        context['produccion_persona'] = produccion_persona

        return context


class ProduccionProyecto(LoginRequiredMixin, TemplateView):
    template_name = 'recursos/produccion-proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProduccionPersona, self).get_context_data(**kwargs)
        personas = Usuario.objects.all()

        produccion_persona = list()
        for persona in personas:
            personas = Produccion.objects.filter(usuario=persona)
            produccion_persona.append(
                {
                    'persona': persona.primer_nombre + ' ' +
                    persona.primer_apellido,
                    'documentos': len(personas)
                }
            )

        context['produccion_persona'] = produccion_persona

        return context
