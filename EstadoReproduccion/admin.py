from django.contrib import admin
from .models import EstadoReproduccion

# Register your models here.
@admin.register(EstadoReproduccion)
class AdminEstadoReproduccion(admin.ModelAdmin):
    list_display = ('id_estado',)
    list_filter = ('nombre',)
