from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novaPessoa/', views.nova_pessoa, name='nova_pessoa'),
    path('alterarPessoa/<int:id_pessoa>/', views.alterar_pessoa, name='alterar_pessoa'),
    path('excluir/<int:id_pessoa>/', views.excluir_pessoa, name='excluir_pessoa'),
]