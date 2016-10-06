from django.contrib import admin
from .models import Medidas

# Register your models here.
@admin.register(Medidas)
class AdminMedidas(admin.ModelAdmin):
    list_display = ('id_medida',)
    list_filter = ('id_bovino',)
