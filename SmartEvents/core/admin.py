from django.contrib import admin
from .models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_hora', 'lugar', 'valor', 'plazas_disponibles')
    list_filter = ('fecha_hora', 'lugar')
    search_fields = ('titulo',)
    filter_horizontal = ('asistentes',)

admin.site.register(Evento, EventoAdmin)


