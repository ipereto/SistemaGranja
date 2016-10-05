from django.contrib import admin
from .models import EstadoGranja
# Register your models here.
@admin.register(EstadoGranja)
class AdminGranja(admin.ModelAdmin):
    list_display = ('id_estado','nombre',)
    list_filter = ('nombre',)
