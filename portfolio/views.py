from django.shortcuts import render, redirect
from .models import Licenciatura, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, Formacao
from .forms import ProjetoForm


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})


def projetos_view(request):
    projetos = Projeto.objects.select_related('uc').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})


def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})


def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)
    return render(request, 'portfolio/projeto.html', {'projeto': projeto})


def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/novo_projeto.html', {'form': form})


def edita_projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/edita_projeto.html', {'form': form, 'projeto': projeto})


def apaga_projeto_view(request, id):
    Projeto.objects.get(id=id).delete()
    return redirect('projetos')
