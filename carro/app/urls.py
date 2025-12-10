from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
]
