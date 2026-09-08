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

class Inscricao(models.Model):
  evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
  participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='inscricoes')
  data_inscricao = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.participante.nome} - inscrito no evento: {self.evento.titulo}"
