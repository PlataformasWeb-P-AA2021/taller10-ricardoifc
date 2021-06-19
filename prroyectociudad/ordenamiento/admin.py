from django.contrib import admin
from ordenamiento.models import Parroquia, Barrio

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):

    list_display = ('id', 'nombre', 'numViviendas', 'numParques', 'numEdificios', 'parroquia')
    search_fields = ('nombre')
admin.site.register(Barrio, BarrioAdmin)