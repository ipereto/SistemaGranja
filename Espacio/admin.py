from django.contrib import admin
from .models import Espacio

# Register your models here.
@admin.register(Espacio)
class AdminEspacio(admin.ModelAdmin):
    list_display = ('id_espacio',)
    list_filter = ('id_espacio',)
