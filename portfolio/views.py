from django.shortcuts import render, redirect
from .models import Licenciatura, UnidadeCurricular, Projeto, Tecnologia, TFC, Competencia, Formacao
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm


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


def tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)
    return render(request, 'portfolio/tecnologia.html', {'tecnologia': tecnologia})


def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/nova_tecnologia.html', {'form': form})


def edita_tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)
    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'portfolio/edita_tecnologia.html', {'form': form, 'tecnologia': tecnologia})


def apaga_tecnologia_view(request, id):
    Tecnologia.objects.get(id=id).delete()
    return redirect('tecnologias')


def competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)
    return render(request, 'portfolio/competencia.html', {'competencia': competencia})


def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/nova_competencia.html', {'form': form})


def edita_competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)
    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/edita_competencia.html', {'form': form, 'competencia': competencia})


def apaga_competencia_view(request, id):
    Competencia.objects.get(id=id).delete()
    return redirect('competencias')


def formacao_view(request, id):
    formacao = Formacao.objects.get(id=id)
    return render(request, 'portfolio/formacao.html', {'formacao': formacao})


def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/nova_formacao.html', {'form': form})


def edita_formacao_view(request, id):
    formacao = Formacao.objects.get(id=id)
    if request.POST:
        form = FormacaoForm(request.POST or None, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)
    return render(request, 'portfolio/edita_formacao.html', {'form': form, 'formacao': formacao})


def apaga_formacao_view(request, id):
    Formacao.objects.get(id=id).delete()
    return redirect('formacoes')
