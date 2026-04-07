import os
import sys
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
    'Carlos Alberto Teixeira Iglesias',
    'Cristiane Ferreira',
    'Cristina Maria Ribeiro Guerra',
    'Daniel Filipe Sobral Fernandes',
    'Daniel Tomas De Maia Mozart Silveira',
    'Diogo Soares Pereira Gil Morais',
    'Duarte Nuno Donas Botto Neves',
    'Francisco Fernandes Castro Rego',
    'Muratore, Giosue',
    'Herminio Miguel Sobral Tavares',
    'Houda Harkat',
    'Iolanda Raquel Fernandes Velho',
    'Joao Caldeira',
    'Joao Licinio Cabral Da Silva',
    'Joao Pedro Cunha Da Silva Eleuterio',
    'Joao Pedro Craveiro',
    'Joao Pedro Lavadinho Moreira',
    'Jose Alexandre Silva Paredes',
    'Jose Cascais Bras',
    'Leonardo De Carlo',
    'Lucio Studer Ferreira',
    'Luis Gomes',
    'Luis Filipe Duarte Sousa',
    'Manuel Pita',
    'Marcelo Garcia Domingues',
    'Maria Da Conceicao Goncalves Costa',
    'Maria Jose De Almeida E Silva',
    'Marina Pereira Martins',
    'Martim Duarte Barja Mourao',
    'Paulo Jorge Tavares Guedes',
    'Pedro Arroz Correia Bonifacio Serra',
    'Pedro De Almeida Perdigao',
    'Pedro Hugo De Queiros Alves',
    'Ricardo Jorge Serras Santos',
    'Rodrigo Coutinho Correia',
    'Rui Filipe Guimaraes Dos Santos',
    'Rui Ribeiro',
    'Rute Maria Da Silva Proenca Muchacho',
    'Sergio Pedro Mestre Ferreira',
    'Sergio Rodrigues Nunes',
    'Sofia Da Silva Fernandes',
    'Sofia Naique',
    'Thiago Gustavo Vieira De Paiva',
    'Tomaz Saraiva',
    'Zuil Pirola',
]


def load_docentes():
    criados = existentes = erros = 0

    for nome in DOCENTES:
        try:
            obj, created = Docente.objects.get_or_create(
                nome=nome,
                defaults={
                    'email':       '',
                    'url_lusofona': '',
                    'foto':        None,
                }
            )
            status = 'CRIADO' if created else 'JA EXISTE'
            print(f'  [{status}] {obj.nome}')
            if created:
                criados += 1
            else:
                existentes += 1
        except Exception as e:
            erros += 1
            print(f'  [ERRO] {nome}: {e}')

    print(f'\n=== Resultado ===')
    print(f'Criados:     {criados}')
    print(f'Ja existiam: {existentes}')
    print(f'Erros:       {erros}')
    print(f'Total:       {criados + existentes}')


def load_makingof():
    obj, created = MakingOf.objects.get_or_create(
        titulo='Modelacao dos Docentes',
        entidade_relacionada='Docente',
        defaults={
            'descricao': (
                'Carreguei 51 docentes do curso LEI retirados do site da Lusofona.'
            ),
            'decisoes_tomadas': (
                'Decidi incluir nome, email, url_lusofona e foto. O campo url_lusofona '
                'e importante para ligar a pagina pessoal do docente no site da Lusofona, '
                'conforme o enunciado. Os emails e URLs serao preenchidos manualmente no admin.'
            ),
            'erros_correcoes': (
                'Alguns nomes tinham formatacao invertida (ex: Muratore, Giosue) - foram '
                'mantidos como estavam na fonte original.'
            ),
            'uso_ia': (
                'Utilizei o Claude para estruturar o script. A lista de docentes foi '
                'retirada do site da Lusofona.'
            ),
        }
    )
    status = 'CRIADO' if created else 'JA EXISTE'
    print(f'\nMaking Of: [{status}] {obj.titulo}')


if __name__ == '__main__':
    print('A carregar docentes...\n')
    load_docentes()
    load_makingof()
    print('\nConcluido.')
