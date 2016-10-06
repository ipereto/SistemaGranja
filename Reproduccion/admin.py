from django.contrib import admin
from .models import Reproduccion

# Register your models here.
@admin.register(Reproduccion)
class AdminReproduccion(admin.ModelAdmin):
    list_display = ('id_reproduccion',)
    list_filter = ('id_bovino',)
