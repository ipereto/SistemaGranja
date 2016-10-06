from django.contrib import admin
from .models import Bovino

# Register your models here.
@admin.register(Bovino)
class AdminBovino(admin.ModelAdmin):
    list_display = ('id_bovino',)
    list_filter = ('id_bovino',)
