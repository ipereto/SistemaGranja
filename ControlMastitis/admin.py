from django.contrib import admin
from .models import ControlMastitis

# Register your models here.
@admin.register(ControlMastitis)
class AdminControlMastitis(admin.ModelAdmin):
    list_display = ('id_control',)
    list_filter = ('id_bovino',)
