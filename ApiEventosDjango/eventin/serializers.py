from rest_framework import serializers
from .models import Evento, Participante, Inscricao
from .validators import validate_nome, validate_email, validate_telefone, validate_cpf

class EventoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Evento
    fields = ['id', 'titulo', 'descricao', 'data_evento', 'local', 'capacidade']

class ParticipanteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Participante
    fields = ['id', 'nome', 'cpf', 'email', 'telefone']

  def validate_nome(self, nome):
    return validate_nome(nome)
  def validate_email(self, email):
    return validate_email(email)
  def validate_telefone(self, telefone):
    return validate_telefone(telefone)
  def validate_cpf(self, cpf):
    return validate_cpf(cpf)


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