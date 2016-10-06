from django.contrib import admin
from .models import ViaAplicacion

# Register your models here.
@admin.register(ViaAplicacion)
class AdminViaAplicacion(admin.ModelAdmin):
    list_display = ('id_via_apli',)
    list_filter = ('nombre',)
