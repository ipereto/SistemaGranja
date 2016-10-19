# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Raza.models import Raza
from Granja.models import Granja
from TipoParto.models import TipoParto
from Procedencia.models import Procedencia
from EstadoBovino.models import EstadoBovino
from Etapa.models import Etapa
from Sexo.models import Sexo
from datetime import datetime
#from .models import Bovino
# Create your models here.
class Bovino(models.Model):
    id_bovino = models.CharField(primary_key=True, max_length=140,verbose_name="Identificación del bovino")
    nombre = models.CharField(max_length=50,default=None,verbose_name="Nombre")
    id_raza = models.OneToOneField(Raza, default=None,verbose_name="Raza")
    id_padre = models.OneToOneField('self', related_name='id_padre_bovino', blank=True, null=True,verbose_name="Identificación del bovino padre")
    id_madre = models.OneToOneField('self', related_name='id_madre_bovino', blank=True, null=True,verbose_name="Identificación del bovino madre")
    id_granja = models.OneToOneField(Granja,default=None,verbose_name="Granja a la que pertenece")
    id_parto = models.OneToOneField(TipoParto,default=None,verbose_name="Tipo de parto")
    id_procedencia = models.OneToOneField(Procedencia,default=None,verbose_name="Procedencia")
    id_estado = models.OneToOneField(EstadoBovino,default=None,verbose_name="Estado")
    id_etapa = models.OneToOneField(Etapa,default=None,verbose_name="Etapa")
    id_sexo = models.OneToOneField(Sexo,default=None,verbose_name="Sexo")
    fecha_nacimiento = models.DateTimeField(verbose_name='Fecha de nacimiento',default=None)
    peso_nacimiento = models.DecimalField(max_digits=5,decimal_places=2,default=None,verbose_name="Peso de nacimiento")
    fecha_destete = models.DateTimeField(verbose_name='Fecha de destete',default=None,blank=True,null=True)
    edad_primer_parto = models.IntegerField(verbose_name='Edad del primer parto',default=None,blank=True,null=True)
    fechaEntrada = models.DateTimeField(verbose_name='Fecha de entrada', default=None)
    fechaSalida = models.DateTimeField(verbose_name='Fecha de salida',default=None, blank=True,null=True)
    motivo_salida = models.TextField(max_length=140,default=None, blank=True,null=True, verbose_name="Motivo de salida")
    fecha_primer_servicio = models.DateTimeField(verbose_name='Fecha de primer servicio',default=None, blank=True,null=True)

    def __str__(self):
        return self.id_bovino

    class Meta:
        ordering = ('id_bovino', )
