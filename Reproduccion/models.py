from __future__ import unicode_literals

from django.db import models
from Servicio.models import Servicio
from SemenToro.models import SemenToro
from Bovino.models import Bovino
from EstadoReproduccion.models import EstadoReproduccion

# Create your models here.
class Reproduccion(models.Model):
    id_reproduccion = models.AutoField(primary_key=True)
    id_bovino = models.ForeignKey(Bovino, db_constraint=True, swappable=True, related_name='id_reproduccion_bovino')
    id_toro = models.ForeignKey(Bovino, db_constraint=True, swappable=True, related_name='id_reproduccion_toro',blank=True, default=None)
    id_servicio = models.ForeignKey(Servicio, related_name='id_reproduccion_servicio')
    id_cria = models.ForeignKey(Bovino, db_constraint=True, swappable=True, related_name='id_reproduccion_cria',blank=True, default=None)
    id_semen_toro = models.ForeignKey(SemenToro, db_constraint=True, swappable=True, related_name='id_reproduccion_semen',blank=True, default=None)
    fecha_servicio = models.DateTimeField()
    proximoCelo = models.DateTimeField()
    fechaPosibleParto = models.DateTimeField(blank=True)
    fechaSecado = models.DateTimeField(blank=True)
    cantCelosPosParto = models.IntegerField(default=None,blank=True)
    id_estado = models.ForeignKey(EstadoReproduccion, related_name='id_reproduccion_estado',default=None)

    def __str__(self):
        return str(self.id_reproduccion)

    class Meta:
        ordering = ('id_reproduccion', )

    def __unicode__(self):
        return str(self.id_reproduccion)
