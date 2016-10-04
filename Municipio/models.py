from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id_municipio

    class Meta:
        ordering = ('id_municipio', )
