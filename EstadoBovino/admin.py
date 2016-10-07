from django.contrib import admin
from .models import EstadoBovino

# Register your models here.
@admin.register(EstadoBovino)
class AdminEstadoBovino(admin.ModelAdmin):
    list_display = ('id_estado','nombre')
    list_filter = ('nombre',)
