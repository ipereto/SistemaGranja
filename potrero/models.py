from __future__ import unicode_literals

from django.db import models
from granja.models import Granja

# Create your models here.
class Potrero(models.Model):
    id_potrero = models.CharField(max_length=50)
    id_granja = models.CharField(max_length=50)
    capacidad = models.DecimalField(max_digits=6,decimal_places=2)
    area = models.DecimalField(max_digits=6,decimal_places=2)
    estado = models.CharField(max_length=50)
    aforo = area = models.DecimalField(max_digits=6,decimal_places=2)
    area = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.id_potrero

    class Meta:
        ordering = ('id', )

class Granja_Potrero(models.Model):
    granja = models.ForeignKey(Granja)
    potrero = models.ForeignKey(Potrero)

    class  Meta:
        verbose_name = 'Relacion granja y potrero'

    def __str__(self):
        return '%s %s' % (self.granja.id_granja, self.potrero.id_potrero)
