from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
@login_required
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'home.html', {'pessoas': pessoas})

@login_required
def nova_pessoa(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')

        Pessoa.objects.create(
            nome=nome,
            email=email,
            data_nascimento=data_nascimento
        )

        return redirect('home')

    return render(request, 'nova_pessoa.html')