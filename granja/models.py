from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Granja(models.Model):
    id_granja = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    precipitacion = models.DecimalField(max_digits=6,decimal_places=2)
    altitud = models.DecimalField(max_digits=6,decimal_places=2)
    zona_vida = models.CharField(max_length=50)
    humedad_relativa = models.DecimalField(max_digits=6,decimal_places=2)
    temp_prom = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.nombre
