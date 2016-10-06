from django.contrib import admin
from .models import EstadoPalpacion

# Register your models here.
@admin.register(EstadoPalpacion)
class AdminEstadoPalpacion(admin.ModelAdmin):
    list_display = ('id_estado',)
    list_filter = ('nombre',)
