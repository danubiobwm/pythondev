from rest_framework import viewsets, generics
from .models import Evento, Participante, Inscricao
from .serializers import EventoSerializer, ParticipanteSerializer, InscricaoSerializer, ListInscricaoParticipanteSerializer, ListInscricaoEventoSerializer

class EventosViewSet(viewsets.ModelViewSet):
  queryset = Evento.objects.all()
  serializer_class = EventoSerializer

class ParticipantesViewSet(viewsets.ModelViewSet):
  queryset = Participante.objects.all()
  serializer_class = ParticipanteSerializer

class InscricoesViewSet(viewsets.ModelViewSet):
  queryset = Inscricao.objects.all()
  serializer_class = InscricaoSerializer


class ListInscricaoParticipante(generics.ListAPIView):
  serializer_class = ListInscricaoParticipanteSerializer
  def get_queryset(self):
    participante_id = self.kwargs['pk']
    return Inscricao.objects.filter(participante_id=participante_id)

class ListInscricaoEvento(generics.ListAPIView):
  serializer_class = ListInscricaoEventoSerializer
  def get_queryset(self):
    evento_id = self.kwargs['pk']
    return Inscricao.objects.filter(evento_id=evento_id)