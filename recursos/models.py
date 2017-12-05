from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proyecto'
        verbose_name_plural = 'Proyectos'


class Serie(models.Model):
    nombre = models.CharField(max_length=200)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'serie'
        verbose_name_plural = 'Series'


class Perfil(models.Model):
    nombre = models.CharField(max_length=200)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'perfil'
        verbose_name_plural = 'Perfiles'


class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200, blank=True)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200, blank=True)
    identificacion = models.CharField(max_length=200)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.primer_nombre + ' ' + self.segundo_nombre

    class Meta:
        db_table = 'usuario'
        verbose_name_plural = 'Usuarios'


class Actividad(models.Model):
    nombre = models.CharField(max_length=200)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'actividad'
        verbose_name_plural = 'Actividades'


class OrdenTrabajo(models.Model):
    numero = models.CharField(max_length=50)
    fecha_recepcion = models.DateTimeField()

    def __str__(self):
        return self.numero

    class Meta:
        db_table = 'orden_trabajo'
        verbose_name_plural = 'Ordenes de trabajo'


class Documento(models.Model):
    sticker = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField()
    orden_trabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)

    def __str__(self):
        return self.sticker

    class Meta:
        db_table = 'documento'
        verbose_name_plural = 'Documentos'


class Produccion(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return self.documento.sticker

    class Meta:
        db_table = 'produccion'
        verbose_name_plural = 'Producciones'


class UsuarioProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.proyecto.nombre

    class Meta:
        db_table = 'usuario_proyecto'
        verbose_name_plural = 'Usuarios de Proyecto'

    def cantidad_usuarios(self):
        return UsuarioProyecto.objects.filter(proyecto=self.proyecto).count()
