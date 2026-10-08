from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.
@login_required
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'home.html', {'pessoas': pessoas})

@login_required
def nova_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PessoaForm()

    return render(request, 'nova_pessoa.html', {'form': form})

# NOTE: código antigo @login_required
# def alterar_pessoa(request, id_pessoa):
#     pessoa = Pessoa.objects.get(id_pessoa=id_pessoa)
#     if request.method == 'POST':
#         pessoa.nome = request.POST.get('nome')
#         pessoa.email = request.POST.get('email')
#         pessoa.data_nascimento = request.POST.get('data_nascimento')

#         pessoa.save()

#         return redirect('home')
#     return render(request, 'alterar_pessoa.html', {'pessoa': pessoa})

@login_required
def alterar_pessoa(request, id_pessoa):
    pessoa = Pessoa.objects.get(id_pessoa=id_pessoa)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'alterar_pessoa.html', {
        'form': form,
        'pessoa': pessoa,
    })

@login_required
def excluir_pessoa(request, id_pessoa):
    pessoa = Pessoa.objects.get(id_pessoa=id_pessoa)
    pessoa.delete()
    return redirect('home')