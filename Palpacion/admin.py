from django.contrib import admin
from .models import Palpacion

# Register your models here.
@admin.register(Palpacion)
class AdminPalpacion(admin.ModelAdmin):
    list_display = ('id_palpacion',)
    list_filter = ('id_palpacion',)
