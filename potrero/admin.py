from django.contrib import admin
from .models import Potrero, Granja_Potrero

# Register your models here.
@admin.register(Potrero)
class AdminPotrero(admin.ModelAdmin):
    list_display = ('id_potrero','capacidad','area','estado','id_granja','aforo','area',)
    list_filter = ('id',)


@admin.register(Granja_Potrero)
class AdminGranja_Potrero(admin.ModelAdmin):
    list_display = ('potrero','granja',)
