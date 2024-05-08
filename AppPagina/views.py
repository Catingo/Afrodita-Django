from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Inicio(request):
    return render(request, "AppPagina/Inicio.html")


def Servicios(request):
    #return HttpResponse("Esta es la página de SERVICIOS")
    return render(request, "AppPagina/Servicios.html")
