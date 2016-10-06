from django.contrib import admin
from .models import EntregaLeche

# Register your models here.
@admin.register(EntregaLeche)
class AdminEntregaLeche(admin.ModelAdmin):
    list_display = ('id_ent_leche',)
    list_filter = ('id_ent_leche',)
