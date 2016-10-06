from django.contrib import admin
from .models import Raza

# Register your models here.
@admin.register(Raza)
class AdminRaza(admin.ModelAdmin):
    list_display = ('id_raza','nombre')
    list_filter = ('nombre',)
