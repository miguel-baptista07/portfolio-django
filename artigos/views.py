from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm


def artigos_view(request):
    artigos = Artigo.objects.prefetch_related('likes', 'comentarios').select_related('autor').all()
    is_autor = request.user.is_authenticated and request.user.groups.filter(name='autores').exists()
    return render(request, 'artigos/artigos.html', {'artigos': artigos, 'is_autor': is_autor})


def artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    form_comentario = ComentarioForm()
    if request.method == 'POST':
        if 'like' in request.POST:
            ip = request.META.get('REMOTE_ADDR')
            Like.objects.get_or_create(artigo=artigo, utilizador=ip)
            return redirect('artigo', artigo_id=artigo_id)
        if request.user.is_authenticated and 'comentario' in request.POST:
            form_comentario = ComentarioForm(request.POST)
            if form_comentario.is_valid():
                c = form_comentario.save(commit=False)
                c.artigo = artigo
                c.autor = request.user
                c.save()
                return redirect('artigo', artigo_id=artigo_id)
    is_autor = request.user.is_authenticated and request.user.groups.filter(name='autores').exists()
    return render(request, 'artigos/artigo.html', {'artigo': artigo, 'form_comentario': form_comentario, 'is_autor': is_autor})


@login_required
def novo_artigo_view(request):
    if not request.user.groups.filter(name='autores').exists():
        return redirect('artigos')
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')
    return render(request, 'artigos/novo_artigo.html', {'form': form})


@login_required
def edita_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if artigo.autor != request.user:
        return redirect('artigos')
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigo', artigo_id=artigo_id)
    return render(request, 'artigos/edita_artigo.html', {'form': form, 'artigo': artigo})
