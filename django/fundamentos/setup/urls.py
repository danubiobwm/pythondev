
from django.contrib import admin
from django.urls import path

from .views import aboutpage, homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about', aboutpage, name='about')
]
