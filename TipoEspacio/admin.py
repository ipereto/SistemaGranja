from django.contrib import admin
from .models import TipoEspacio

# Register your models here.
@admin.register(TipoEspacio)
class AdminTipoEspacio(admin.ModelAdmin):
    list_display = ('id_tipo',)
    list_filter = ('nombre',)
