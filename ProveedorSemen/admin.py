from django.contrib import admin
from .models import ProveedorSemen

# Register your models here.
@admin.register(ProveedorSemen)
class AdminProveedor(admin.ModelAdmin):
    list_display = ('nit',)
