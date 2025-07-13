from django.contrib import admin
from cars.models import Car  # Importando o modelo Car do arquivo models.py
from cars.models import Brand  # Importando o modelo Brand do arquivo models.py

# Registrar o modelo Car no admin do Django
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') # Campos a serem exibidos na lista
    search_fields = ('model','brand') # Campos a serem pesquisados

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Campos a serem exibidos na lista
    search_fields = ('name',)  # Campos a serem pesquisados

admin.site.register(Car, CarAdmin) # Registrar o modelo Car com as configurações definidas
admin.site.register(Brand, BrandAdmin) # Registrar o modelo Brand com as configurações definidas