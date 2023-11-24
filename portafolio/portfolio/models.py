from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(max_length=250, verbose_name="Descripción")
    image = models.ImageField(
        upload_to="projects", verbose_name="Imagen"
    )  # El diccionario projects se crea al subir la imagen
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    url = models.URLField(blank=True, null=True, verbose_name="Enlace")

    def __str__(self):
        return self.title  # pone el nombre del proyecto

    class Meta:
        verbose_name = "proyecto"  # traduce el nombre de la app
        verbose_name_plural = "proyectos"  # traduce el nombre de la app
        ordering = ["-created"]  # ordena las publicaciones de mas nuevo a mas viejo
