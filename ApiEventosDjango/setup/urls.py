
from django.contrib import admin
from django.urls import path
from eventin.views import participantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('participantes/', participantes),
]
