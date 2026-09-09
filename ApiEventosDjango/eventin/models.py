from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

# Create your models here.

class Evento(models.Model):
  titulo = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
  descricao = models.TextField(validators=[MinLengthValidator(10)])
  local = models.CharField(max_length=100, validators=[MinLengthValidator(6)])
  data_evento = models.DateField()
  horario = models.TimeField()
  capacidade = models.PositiveIntegerField(validators=[MinLengthValidator(1)])

  def __str__(self):
    return self.titulo

class Participante(models.Model):
  nome = models.CharField(max_length=100, validators=[MinLengthValidator(4)])
  cpf = models.CharField(max_length=11, unique=True, validators=[MinLengthValidator(11)])
  email = models.EmailField(unique=True, validators=[EmailValidator()])
  telefone = models.CharField(max_length=15, blank=True)

  def __str__(self):
    return self.nome

class Inscricao(models.Model):
  evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
  participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='inscricoes')
  data_inscricao = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.participante.nome} - inscrito no evento: {self.evento.titulo}"
