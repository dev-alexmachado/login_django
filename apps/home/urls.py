from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novaPessoa/', views.nova_pessoa, name='nova_pessoa'),
]