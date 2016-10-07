from django.contrib import admin
from .models import TipoParto

# Register your models here.
@admin.register(TipoParto)
class AdminTipoParto(admin.ModelAdmin):
    list_display = ('id_parto','nombre')
    list_filter = ('nombre',)
