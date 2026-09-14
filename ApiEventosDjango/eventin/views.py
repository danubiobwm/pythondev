from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Evento, Participante, Inscricao
from .serializers import EventoSerializer, ParticipanteSerializer, InscricaoSerializer, ListInscricaoParticipanteSerializer, ListInscricaoEventoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EventosViewSet(viewsets.ModelViewSet):
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  queryset = Evento.objects.all()
  serializer_class = EventoSerializer

class ParticipantesViewSet(viewsets.ModelViewSet):
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  queryset = Participante.objects.all()
  serializer_class = ParticipanteSerializer
  filter_backends = [DjangoFilterBackend,  filters.OrderingFilter , filters.SearchFilter]
  ordering_fields = ['nome']
  search_fields = ['nome', 'cpf']

class InscricoesViewSet(viewsets.ModelViewSet):
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
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