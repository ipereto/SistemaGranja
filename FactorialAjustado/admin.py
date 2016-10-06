from django.contrib import admin
from .models import FactorialAjustado

# Register your models here.
@admin.register(FactorialAjustado)
class AdminFactorialAjustado(admin.ModelAdmin):
    list_display = ('id_factorial',)
    list_filter = ('id_factorial',)
