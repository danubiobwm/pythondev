from django.http import HttpResponse

def homepage(request):
  return HttpResponse("Hello world")


def aboutpage(request):
  return HttpResponse("Page About")