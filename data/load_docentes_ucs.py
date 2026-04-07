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
    },
    {
        'nome':         'Lucio Studer Ferreira',
        'email':        'lucio.studer@ulusofona.pt',
        'url_lusofona': 'https://www.ulusofona.pt/docentes/lucio-miguel-studer-ferreira-6069',
    },
    {
        'nome':         'Pedro Hugo De Queirós Alves',
        'email':        'pedro.alves@ulusofona.pt',
        'url_lusofona': 'https://www.ulusofona.pt/docentes/pedro-hugo-de-queiros-alves-4997',
    },
]


if __name__ == '__main__':
    # 1. Apagar todos os docentes existentes
    deleted, _ = Docente.objects.all().delete()
    print(f'Docentes apagados: {deleted}\n')

    # 2. Criar os 3 docentes
    docentes = []
    for d in DOCENTES:
        obj = Docente.objects.create(
            nome=d['nome'],
            email=d['email'],
            url_lusofona=d['url_lusofona'],
            foto=None,
        )
        docentes.append(obj)
        print(f'  [CRIADO] {obj.nome}')
        print(f'           {obj.email}')
        print(f'           {obj.url_lusofona}')

    # 3. Associar os 3 docentes a todas as UCs
    ucs = UnidadeCurricular.objects.all()
    print(f'\nA associar {len(docentes)} docentes a {ucs.count()} UCs...')
    for uc in ucs:
        uc.docentes.set(docentes)

    print(f'\n=== Resultado ===')
    print(f'Docentes criados: {len(docentes)}')
    print(f'UCs atualizadas:  {ucs.count()}')
    print('\nConcluído.')
