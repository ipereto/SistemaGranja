from django.contrib import admin
from .models import Bovino

# Register your models here.
@admin.register(Bovino)
class AdminBovino(admin.ModelAdmin):
    list_display = (
    'id_bovino',
    'id_raza',
    'id_padre',
    'id_madre',
    'id_granja',
    'id_parto',
    'id_procedencia',
    'id_estado',
    'id_etapa',
    'id_sexo',
    'nombre',
    'fecha_nacimiento',
    'peso_nacimiento',
    'fecha_destete',
    'edad_primer_parto',
    'fechaEntrada',
    'fechaSalida',
    'motivo_salida',
    'fecha_primer_servicio',
    )
    list_filter = ('id_bovino',)
