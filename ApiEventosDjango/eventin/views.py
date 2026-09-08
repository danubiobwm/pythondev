from rest_framework import viewsets
from .models import Evento, Participante, Inscricao
from .serializers import EventoSerializer, ParticipanteSerializer, InscricaoSerializer

class EventosViewSet(viewsets.ModelViewSet):
  queryset = Evento.objects.all()
  serializer_class = EventoSerializer

class ParticipantesViewSet(viewsets.ModelViewSet):
  queryset = Participante.objects.all()
  serializer_class = ParticipanteSerializer

class InscricoesViewSet(viewsets.ModelViewSet):
  queryset = Inscricao.objects.all()
  serializer_class = InscricaoSerializer