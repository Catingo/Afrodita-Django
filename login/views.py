from django.shortcuts import render
from django.http import HttpResponse

# Aqui van mis views
def chao(request):
    return HttpResponse("<H1>Chao esta es mi página principal LOGIN</H1>")
