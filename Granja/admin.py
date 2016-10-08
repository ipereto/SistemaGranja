from django.contrib import admin
from .models import Granja
from  Departamento.models import Departamento
from  Municipio.models import Municipio

# Register your models here.
#admin.site.register(Granja)
@admin.register(Granja)
class AdminGranja(admin.ModelAdmin):
    list_display = (
    'id_granja',
    'nombre',
    'altitud',
    'id_estado',
    'id_departamento',
    'id_municipio',
    'direccion',
    'precipitacion',
    'zona_vida',
    'humedad_relativa',
    'temp_prom',)
    list_filter = ('nombre',)
    # def get_form(self, request, obj, **kwargs):
    #     form = super(AdminGranja, self).get_form(request, obj, **kwargs)
    #     form.base_fields['id_municipio'].queryset = obj.Departamento.all()
    #     return form
