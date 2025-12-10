from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Carro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco', 'vendido')
    list_filter = ('marca', 'vendido')
    search_fields = ('marca', 'modelo')
