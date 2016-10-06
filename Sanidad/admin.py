from django.contrib import admin
from .models import Sanidad

# Register your models here.
@admin.register(Sanidad)
class AdminSanidad(admin.ModelAdmin):
    list_display = ('id_sanidad',)
    list_filter = ('id_bovino',)
