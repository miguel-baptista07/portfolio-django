# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import Docente, MakingOf

DOCENTES = [
    'Ana Vieira Dos Santos Cruz',
    'Andre Vieira Vassalo Da Fonseca',
    'Berend Willem Martijn Kuipers',
    'Brena Kelly Sousa Lima',
    'Bruno D. Ferreira-saraiva',
    'Bruno Miguel Pereira Cipriano',
    'Carlos Alberto Teixeira Iglésias',
    'Cristiane Ferreira',
    'Cristina Maria Ribeiro Guerra',
    'Daniel Filipe Sobral Fernandes',
    'Daniel Tomás De Maia Mozart Silveira',
    'Diogo Soares Pereira Gil Morais',
    'Duarte Nuno Donas Botto Neves',
    'Francisco Fernandes Castro Rego',
    'Muratore, Giosuè',
    'Herminio Miguel Sobral Tavares',
    'Houda Harkat',
    'Iolanda Raquel Fernandes Velho',
    'João Caldeira',
    'João Licinio Cabral Da Silva',
    'João Pedro Cunha Da Silva Eleutério',
    'João Pedro Craveiro',
    'João Pedro Lavadinho Moreira',
    'José Alexandre Silva Paredes',
    'José Cascais Brás',
    'Leonardo De Carlo',
    'Lucio Studer Ferreira',
    'Luis Gomes',
    'Luís Filipe Duarte Sousa',
    'Manuel Pita',
    'Marcelo Garcia Domingues',
    'Maria Da Conceição Gonçalves Costa',
    'Maria José De Almeida E Silva',
    'Marina Pereira Martins',
    'Martim Duarte Barja Mourão',
    'Paulo Jorge Tavares Guedes',
    'Pedro Arroz Correia Bonifácio Serra',
    'Pedro De Almeida Perdigão',
    'Pedro Hugo De Queirós Alves',
    'Ricardo Jorge Serras Santos',
    'Rodrigo Coutinho Correia',
    'Rui Filipe Guimarães Dos Santos',
    'Rui Ribeiro',
    'Rute Maria Da Silva Proença Muchacho',
    'Sergio Pedro Mestre Ferreira',
    'Sérgio Rodrigues Nunes',
    'Sofia Da Silva Fernandes',
    'Sofia Naique',
    'Thiago Gustavo Vieira De Paiva',
    'Tomaz Saraiva',
    'Zuil Pirola',
]


def load_docentes():
    deleted, _ = Docente.objects.all().delete()
    print(f'Docentes apagados: {deleted}\n')

    criados = erros = 0

    for nome in DOCENTES:
        try:
            obj = Docente.objects.create(
                nome=nome,
                email='',
                url_lusofona='',
                foto=None,
            )
            print(f'  [CRIADO] {obj.nome}')
            criados += 1
        except Exception as e:
            erros += 1
            print(f'  [ERRO] {nome}: {e}')

    print(f'\n=== Resultado ===')
    print(f'Criados: {criados}')
    print(f'Erros:   {erros}')
    print(f'Total:   {criados}')


def load_makingof():
    obj, created = MakingOf.objects.update_or_create(
        titulo='Modelação dos Docentes',
        entidade_relacionada='Docente',
        defaults={
            'descricao': (
                'Carreguei 51 docentes do curso LEI retirados do site da Lusófona.'
            ),
            'decisoes_tomadas': (
                'Decidi incluir nome, email, url_lusofona e foto. O campo url_lusofona '
                'é importante para ligar à página pessoal do docente no site da Lusófona, '
                'conforme o enunciado. Os emails e URLs serão preenchidos manualmente no admin.'
            ),
            'erros_correcoes': (
                'Alguns nomes tinham formatação invertida (ex: Muratore, Giosuè) — foram '
                'mantidos como estavam na fonte original.'
            ),
            'uso_ia': (
                'Utilizei o Claude para estruturar o script. A lista de docentes foi '
                'retirada do site da Lusófona.'
            ),
        }
    )
    status = 'CRIADO' if created else 'ATUALIZADO'
    print(f'\nMaking Of: [{status}] {obj.titulo}')


if __name__ == '__main__':
    print('A carregar docentes com acentos...\n')
    load_docentes()
    load_makingof()
    print('\nConcluído.')
