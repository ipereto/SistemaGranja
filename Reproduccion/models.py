# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Servicio.models import Servicio
from SemenToro.models import SemenToro
from Bovino.models import Bovino
from EstadoReproduccion.models import EstadoReproduccion

# Create your models here.
class Reproduccion(models.Model):
    id_reproduccion = models.AutoField(primary_key=True)
    id_bovino = models.ForeignKey(Bovino, db_constraint=True, swappable=True, related_name='id_reproduccion_bovino', verbose_name="Idenficación del bovino")
    id_toro = models.ForeignKey(Bovino, related_name='id_reproduccion_toro',null=True,blank=True, default=None, verbose_name="Idenficación del toro")
    id_servicio = models.ForeignKey(Servicio, related_name='id_reproduccion_servicio', verbose_name="Tipo de servicio")
    id_cria = models.ForeignKey(Bovino, related_name='id_reproduccion_cria',blank=True, default=None, verbose_name="Idenficación de la cría",null=True)
    id_semen_toro = models.ForeignKey(SemenToro, related_name='id_reproduccion_semen',blank=True, default=None, verbose_name="Idenficación del semen del toro",null=True)
    fecha_servicio = models.DateTimeField(verbose_name="Fecha del servicio")
    proximoCelo = models.DateTimeField(verbose_name="Fecha del próximo celo")
    fechaPosibleParto = models.DateTimeField(blank=True, verbose_name="Fecha del posible parto",null=True)
    fechaSecado = models.DateTimeField(blank=True, verbose_name="Fecha de secado",null=True)
    cantCelosPosParto = models.IntegerField(default=None,blank=True, verbose_name="Cantidad de celos posparto",null=True)
    id_estado = models.ForeignKey(EstadoReproduccion, related_name='id_reproduccion_estado',default=None, verbose_name="Estado de la reproducción")

    def __str__(self):
        return str(self.id_reproduccion)

    class Meta:
        ordering = ('id_reproduccion', )

    def __unicode__(self):
        return str(self.id_reproduccion)
