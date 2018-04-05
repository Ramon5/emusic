from django.contrib import admin
from .models import Contratante, Evento


class ContratanteAdmin(admin.ModelAdmin):
    '''
        Admin View for Usuario
    '''

    # mesma funcao do select com while
    list_display = ('NomeContratante', 'EmailContratante', 'Telefone')


class EventoAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('NomeEvento', 'CidadeEvento')


admin.site.register(Contratante, ContratanteAdmin)
admin.site.register(Evento, EventoAdmin)
