from django.contrib import admin
from .models import Medicamento

# Register your models here.
@admin.register(Medicamento)
class AdminMedicamento(admin.ModelAdmin):
    list_display = ('id_medicamento',)
    list_filter = ('producto',)
