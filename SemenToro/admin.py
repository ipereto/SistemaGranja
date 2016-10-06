from django.contrib import admin
from .models import SemenToro

# Register your models here.
@admin.register(SemenToro)
class AdminSemenToro(admin.ModelAdmin):
    list_display = ('id_semen_toro',)
    list_filter = ('id_semen_toro',)
