from __future__ import unicode_literals

from django.db import models
from EstadoGranja.models import EstadoGranja
from ZonaVida.models import ZonaVida

# Create your models here.
class Granja(models.Model):
    id_granja = models.CharField(primary_key=True,max_length=50)
    nombre = models.CharField(max_length=50)
    id_estado = models.OneToOneField(EstadoGranja, related_name='id_granja_estado',default=None)
    id_departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    precipitacion = models.DecimalField(max_digits=6,decimal_places=2)
    altitud = models.DecimalField(max_digits=6,decimal_places=2)
    zona_vida = models.OneToOneField(ZonaVida, related_name='id_granja_zonavida',default=None)
    humedad_relativa = models.DecimalField(max_digits=6,decimal_places=2)
    temp_prom = models.DecimalField(max_digits=6,decimal_places=2)
    mapa = models.ImageField(blank=True)

    def __str__(self):
        return self.id_granja

    class Meta:
        ordering = ('id_granja', )
