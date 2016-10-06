from django.contrib import admin
from .models import Procedencia

# Register your models here.
@admin.register(Procedencia)
class AdminProcedencia(admin.ModelAdmin):
    list_display = ('id_procedencia',)
    list_filter = ('nombre',)
