
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eventin.views import (
    EventosViewSet, ParticipantesViewSet, InscricoesViewSet,
    ListInscricaoParticipante, ListInscricaoEvento
)


router = routers.DefaultRouter()
router.register('eventos', EventosViewSet, basename='Eventos')
router.register('participantes', ParticipantesViewSet, basename='Participantes')
router.register('inscricoes', InscricoesViewSet, basename='Inscricoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/participantes/<int:pk>/inscricoes/', ListInscricaoParticipante.as_view()),
    path('api/eventos/<int:pk>/inscricoes/', ListInscricaoEvento.as_view()),
]
