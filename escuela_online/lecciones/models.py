from django.db import models

class Leccion(models.Model):
    nombre = models.CharField(max_length=100)
    duracion_video = models.IntegerField()
    imagen = models.ImageField(upload_to='lecciones_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nombre