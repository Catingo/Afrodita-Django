from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Inicio(request):
    return HttpResponse("Esta es la página de INICIO!")

def Servicios(request):
    return HttpResponse("Esta es la página de SERVICIOS")
