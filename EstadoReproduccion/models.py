from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EstadoReproduccion(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id_estado', )

    def __unicode__(self):
        return self.nombre
