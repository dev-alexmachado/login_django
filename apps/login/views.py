from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Nome de usuário ou senha inválidos.',
        })

    return render(request, 'login.html')

def cadastrar(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password != confirm_password:
            return render(request, 'cadastrar.html', {
                'error': 'As senhas não coincidem.',
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'cadastrar.html', {
                'error': 'Este nome de usuário já está cadastrado.',
            })

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'cadastrar.html')