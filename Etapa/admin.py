from django.contrib import admin
from .models import Etapa

# Register your models here.
@admin.register(Etapa)
class AdminEtapa(admin.ModelAdmin):
    list_display = ('id_etapa','nombre')
    list_filter = ('nombre',)
