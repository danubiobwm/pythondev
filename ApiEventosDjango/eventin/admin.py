from django.contrib import admin
from .models import Evento, Participante, Inscricao


class Eventos(admin.ModelAdmin):
  list_display = ('id', 'titulo', 'local', 'data_evento', 'capacidade', 'horario')
  list_display_links = ('id', 'titulo')
  search_fields = ('titulo', 'local')
  list_per_page = 10


class Participantes(admin.ModelAdmin):
  list_display = ('id', 'nome', 'cpf', 'email', 'telefone')
  list_display_links = ('id', 'nome')
  search_fields = ('nome', 'email')
  list_per_page = 10


class Inscricoes(admin.ModelAdmin):
  list_display = ('id', 'evento', 'participante', 'data_inscricao')
  list_display_links = ('id',)
  list_per_page = 10


admin.site.register(Evento, Eventos)
admin.site.register(Participante, Participantes)
admin.site.register(Inscricao, Inscricoes)