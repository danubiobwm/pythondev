from django.shortcuts import render

def homepage(request):
  nome = "Danubio"
  return render(request, "home.html", {'nome':nome})


def aboutpage(request):
  frutas={"maça", "Banana", "Melão"}
  return render(request, "about.html", {'frutas':frutas})