
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eventin.views import EventosViewSet, ParticipantesViewSet


router = routers.DefaultRouter()
router.register(r'eventos', EventosViewSet, basename='Eventos')
router.register(r'participantes', ParticipantesViewSet, basename='Participantes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
