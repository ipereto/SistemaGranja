# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from EstadoGranja.models import EstadoGranja
from ZonaVida.models import ZonaVida
from Departamento.models import Departamento
from Municipio.models import Municipio

# Create your models here.
class Granja(models.Model):
    id_granja = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    id_estado = models.OneToOneField(EstadoGranja, related_name='id_granja_estado',default=None, verbose_name="Estado")
    id_departamento = models.OneToOneField(Departamento, related_name='id_granja_departamento',default=None,verbose_name="Departamento")
    id_municipio = models.OneToOneField(Municipio, related_name='id_granja_municipio',default=None,verbose_name="Municipio")
    direccion = models.CharField(max_length=50,verbose_name="Dirección")
    precipitacion = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Precipitación")
    altitud = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Altitud (m)")
    zona_vida = models.OneToOneField(ZonaVida, related_name='id_granja_zonavida',default=None,verbose_name="Zona de vida")
    humedad_relativa = models.DecimalField(max_digits=6,decimal_places=2, verbose_name="Húmedad relativa (%)")
    temp_prom = models.DecimalField(max_digits=6,decimal_places=2, verbose_name="Temperatura promedio (°C)")
    mapa = models.ImageField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id_granja', )

    def __unicode__(self):
        return self.nombre
