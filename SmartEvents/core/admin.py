from django.contrib import admin
from .models import Evento
import locale

locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_hora', 'lugar', 'valor', 'plazas_disponibles', 'dinero_recaudado')
    list_filter = ('fecha_hora', 'lugar')
    search_fields = ('titulo',)
    filter_horizontal = ('asistentes',)


    def dinero_recaudado(self, obj):
        recaudado = obj.valor * obj.asistentes.count()
        return locale.currency(recaudado, grouping=True, symbol=True)
    dinero_recaudado.short_description = 'Dinero Recaudado (CLP)'

admin.site.register(Evento, EventoAdmin)