from django.urls import path
from AppPagina import views

urlpatterns = [
    path('', views.Inicio),
    path('service/', views.Servicios)
]