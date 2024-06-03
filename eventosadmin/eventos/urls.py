# eventos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('evento/<int:id>/', views.detalhe_evento, name='detalhe_evento'),
    path('criar/', views.criar_evento, name='criar_evento'),
    path('editar/<int:id>/', views.editar_evento, name='editar_evento'),
    path('excluir/<int:id>/', views.excluir_evento, name='excluir_evento'),
]
