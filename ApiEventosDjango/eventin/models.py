from django.db import models

# Create your models here.

class Evento(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField()
  local = models.CharField(max_length=100)
  data_evento = models.DateField()
  horario = models.TimeField()
  capacidade = models.PositiveIntegerField()

  def __str__(self):
    return self.titulo

class Participante(models.Model):
  nome = models.CharField(max_length=100)
  cpf = models.CharField(max_length=11)
  email = models.EmailField(unique=True)
  telefone = models.CharField(max_length=15)

  def __str__(self):
    return self.nome

