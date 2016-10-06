from django.contrib import admin
from .models import EstadoEspacio

# Register your models here.
@admin.register(EstadoEspacio)
class AdminEstadoEspacio(admin.ModelAdmin):
    list_display = ('id_estado',)
    list_filter = ('nombre',)
