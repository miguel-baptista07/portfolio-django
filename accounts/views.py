import uuid
from datetime import timedelta

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.utils import timezone

from .forms import RegistoForm
from .models import MagicToken


def login_view(request):
    erro = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projetos')
        else:
            erro = 'Credenciais inválidas'
    return render(request, 'accounts/login.html', {'erro': erro})


def logout_view(request):
    logout(request)
    return redirect('projetos')


def registo_view(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        grupo = Group.objects.get(name='autores')
        user.groups.add(grupo)
        user.save()
        login(request, user)
        return redirect('projetos')
    return render(request, 'accounts/registo.html', {'form': form})


def magic_link_view(request):
    erro = None
    sucesso = None
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = MagicToken.objects.create(user=user)
            link = request.build_absolute_uri(f'/accounts/magic/{token.token}/')
            send_mail(
                'Login no Portfolio',
                f'Clica aqui para entrar: {link}',
                'noreply@portfolio.com',
                [email],
                fail_silently=False,
            )
            sucesso = 'Email enviado! Verifica a tua caixa de entrada.'
        except User.DoesNotExist:
            erro = 'Email não encontrado.'
    return render(request, 'accounts/magic_link.html', {'erro': erro, 'sucesso': sucesso})


def magic_verify_view(request, token):
    try:
        magic = MagicToken.objects.get(token=token)
        if magic.is_valid():
            magic.usado = True
            magic.save()
            login(request, magic.user)
            return redirect('projetos')
        else:
            return render(request, 'accounts/magic_link.html', {'erro': 'Link expirado ou já utilizado.'})
    except MagicToken.DoesNotExist:
        return render(request, 'accounts/magic_link.html', {'erro': 'Link inválido.'})
