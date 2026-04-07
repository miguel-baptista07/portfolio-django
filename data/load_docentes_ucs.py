# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import Docente, UnidadeCurricular

DOCENTES = [
    {
        'nome':         'Berend Willem Martijn Kuipers',
        'email':        'martijn.kuipers@ulusofona.pt',
        'url_lusofona': 'https://www.ulusofona.pt/docentes/berend-willem-martijn-kuipers-8094',
        'uc_codigo':    'AC1',
    },
    {
        'nome':         'Lucio Studer Ferreira',
        'email':        'lucio.studer@ulusofona.pt',
        'url_lusofona': 'https://www.ulusofona.pt/docentes/lucio-miguel-studer-ferreira-6069',
        'uc_codigo':    'PW1',
    },
    {
        'nome':         'Pedro Hugo De Queirós Alves',
        'email':        'pedro.alves@ulusofona.pt',
        'url_lusofona': 'https://www.ulusofona.pt/docentes/pedro-hugo-de-queiros-alves-4997',
        'uc_codigo':    'LP2',
    },
]


if __name__ == '__main__':
    # 1. Apagar todos os docentes existentes
    deleted, _ = Docente.objects.all().delete()
    print(f'Docentes apagados: {deleted}\n')

    # 2. Criar os 3 docentes e associar às UCs
    criados = erros = 0
    for d in DOCENTES:
        try:
            docente = Docente.objects.create(
                nome=d['nome'],
                email=d['email'],
                url_lusofona=d['url_lusofona'],
                foto=None,
            )
            uc = UnidadeCurricular.objects.get(codigo=d['uc_codigo'])
            uc.docentes.add(docente)
            print(f'  [CRIADO] {docente.nome}')
            print(f'           UC: {uc.codigo} - {uc.nome}')
            criados += 1
        except UnidadeCurricular.DoesNotExist:
            print(f'  [ERRO] UC "{d["uc_codigo"]}" nao encontrada para {d["nome"]}')
            erros += 1
        except Exception as e:
            print(f'  [ERRO] {d["nome"]}: {e}')
            erros += 1

    print(f'\n=== Resultado ===')
    print(f'Docentes criados: {criados}')
    print(f'Erros:            {erros}')
    print('\nConcluido.')
