from django.contrib import admin
from .models import EstadoSanidad

# Register your models here.
@admin.register(EstadoSanidad)
class AdminEstadoSanidad(admin.ModelAdmin):
    list_display = ('id_estado',)
    list_filter = ('nombre',)
