from django.contrib import admin
from .models import MantenimientoEspacio

# Register your models here.
#admin.site.register(Granja)
@admin.register(MantenimientoEspacio)
class AdminMantenimientoEspacio(admin.ModelAdmin):
    list_display = ('id_mant_espacio',)
    list_filter = ('id_mant_espacio',)
