from rest_framework import viewsets
from .models import Evento, Participante
from .serializers import EventoSerializer, ParticipanteSerializer

class EventosViewSet(viewsets.ModelViewSet):
  queryset = Evento.objects.all()
  serializer_class = EventoSerializer

class ParticipantesViewSet(viewsets.ModelViewSet):
  queryset = Participante.objects.all()
  serializer_class = ParticipanteSerializer