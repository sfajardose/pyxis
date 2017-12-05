from django.contrib import admin

from recursos.models import (
    Actividad,
    Documento,
    OrdenTrabajo,
    Perfil,
    Produccion,
    Proyecto,
    Serie,
    Usuario,
    UsuarioProyecto
)


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proyecto')


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proyecto')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'primer_nombre',
        'segundo_nombre',
        'primer_apellido',
        'segundo_apellido',
        'identificacion',
        'perfil'
    )


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'serie')


@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha_recepcion')


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('sticker', 'fecha_inicio', 'orden_trabajo')


@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = (
        'documento',
        'actividad',
        'usuario',
        'fecha_inicio',
        'fecha_fin'
    )


@admin.register(UsuarioProyecto)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = (
        'proyecto',
        'usuario',
        'perfil'
    )
