from django.contrib import admin
from .models import Servicio

# Register your models here.
@admin.register(Servicio)
class AdminServicio(admin.ModelAdmin):
    list_display = ('id_servicio',)
    list_filter = ('nombre',)
