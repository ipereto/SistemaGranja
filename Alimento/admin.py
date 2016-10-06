from django.contrib import admin
from .models import Alimento

# Register your models here.
#admin.site.register(Granja)
@admin.register(Alimento)
class AdminAlimento(admin.ModelAdmin):
    list_display = ('id_alimento',)
    list_filter = ('nombre',)
