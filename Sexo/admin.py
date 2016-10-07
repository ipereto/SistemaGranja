from django.contrib import admin
from .models import Sexo

# Register your models here.
@admin.register(Sexo)
class AdminSexo(admin.ModelAdmin):
    list_display = ('id_sexo','nombre',)
    list_filter = ('nombre',)
