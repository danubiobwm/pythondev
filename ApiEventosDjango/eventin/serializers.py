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

class ListInscricaoParticipanteSerializer(serializers.ModelSerializer):
  evento = serializers.ReadOnlyField(source='evento.titulo')
  class Meta:
    model = Inscricao
    fields = ['evento', 'data_inscricao']

class ListInscricaoEventoSerializer(serializers.ModelSerializer):
  participante = serializers.ReadOnlyField(source='participante.nome')
  class Meta:
    model = Inscricao
    fields = ['participante', 'data_inscricao']