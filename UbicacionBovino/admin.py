from django.contrib import admin
from .models import UbicacionBovino

# Register your models here.
@admin.register(UbicacionBovino)
class AdminUbicacionBovino(admin.ModelAdmin):
    list_display = ('id_ubicacion',)
    list_filter = ('id_bovino',)
