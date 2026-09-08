from rest_framework import serializers
from .models import Evento, Participante, Inscricao

class EventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Evento
    fields = ['id', 'titulo', 'descricao', 'data_evento', 'local', 'capacidade']

class ParticipanteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Participante
    fields = ['id', 'nome', 'cpf', 'email', 'telefone']

class InscricaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Inscricao
    fields = ['id', 'evento', 'participante', 'data_inscricao']
