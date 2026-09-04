from django.http import JsonResponse

def participantes(request):
  if request.method == 'GET':
    participante={
      "id": 1,
      "nome": "João da Silva",
      "email": "joao.silva@example.com",
      "telefone": "11999999999",
      "empresa": "Empresa X",
      "cargo": "Desenvolvedor",
      "cidade": "São Paulo",
      "estado": "SP",
      "pais": "Brasil",
      "cep": "1234567890",
      "endereco": "Rua das Flores, 123",
    }
    return JsonResponse(participante)