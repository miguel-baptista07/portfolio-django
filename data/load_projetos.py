import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import Tecnologia, UnidadeCurricular, Projeto, MakingOf

TECNOLOGIAS = [
    {'nome': 'React',       'categoria': 'Frontend',   'nivel_interesse': 5, 'url_oficial': 'https://react.dev',                                              'pontos_destaque': 'Biblioteca para interfaces reativas com componentes reutilizáveis'},
    {'nome': 'Next.js',     'categoria': 'Frontend',   'nivel_interesse': 5, 'url_oficial': 'https://nextjs.org',                                             'pontos_destaque': 'Framework React com SSR e routing automático'},
    {'nome': 'TypeScript',  'categoria': 'Linguagem',  'nivel_interesse': 4, 'url_oficial': 'https://www.typescriptlang.org',                                 'pontos_destaque': 'JavaScript com tipagem estática'},
    {'nome': 'Tailwind CSS','categoria': 'Frontend',   'nivel_interesse': 4, 'url_oficial': 'https://tailwindcss.com',                                        'pontos_destaque': 'Framework CSS utilitário'},
    {'nome': 'SWR',         'categoria': 'Frontend',   'nivel_interesse': 3, 'url_oficial': 'https://swr.vercel.app',                                         'pontos_destaque': 'Hook para data fetching com cache'},
    {'nome': 'Java',        'categoria': 'Linguagem',  'nivel_interesse': 4, 'url_oficial': 'https://www.java.com',                                           'pontos_destaque': 'Linguagem orientada a objetos robusta e multiplataforma'},
    {'nome': 'HTML',        'categoria': 'Frontend',   'nivel_interesse': 4, 'url_oficial': 'https://developer.mozilla.org/en-US/docs/Web/HTML',              'pontos_destaque': 'Linguagem de marcação para estrutura web'},
    {'nome': 'CSS',         'categoria': 'Frontend',   'nivel_interesse': 4, 'url_oficial': 'https://developer.mozilla.org/en-US/docs/Web/CSS',               'pontos_destaque': 'Linguagem de estilos para apresentação web'},
    {'nome': 'JavaScript',  'categoria': 'Linguagem',  'nivel_interesse': 5, 'url_oficial': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript',        'pontos_destaque': 'Linguagem de programação para web interativa'},
]

PROJETOS = [
    {
        'titulo': 'React & Next.js — Frontend Labs & E-Commerce Platform',
        'descricao': (
            'Modern web application built with React and Next.js, focused on component '
            'architecture, state management, and real-world frontend patterns. Inclui '
            'product listing com search e sorting, dynamic routes, shopping cart com '
            'localStorage, favorites system e countries explorer.'
        ),
        'conceitos_aplicados': (
            'Componentes React, estado com hooks, routing dinâmico, data fetching com SWR, '
            'estilos com Tailwind CSS'
        ),
        'url_github': 'https://github.com/miguel-baptista07/Frontend-Labs-E-CommercePlatform',
        'url_demo':   'https://lab11part1.vercel.app/',
        'data_inicio': '2024-09-01',
        'uc_codigo':   'PW1',
        'tecnologias': ['React', 'Next.js', 'TypeScript', 'SWR', 'Tailwind CSS'],
    },
    {
        'titulo': 'The Great Programming Journey',
        'descricao': (
            'Educational board game engine developed in Java, focused on object-oriented '
            'design and game logic. Arquitetura OOP complexa com herança e polimorfismo, '
            'sem uso de instanceof, lógica turn-based com obstáculos, ferramentas e '
            'persistência.'
        ),
        'conceitos_aplicados': (
            'Herança, polimorfismo, encapsulamento, padrões OOP, lógica de jogo'
        ),
        'url_github': 'https://github.com/miguel-baptista07/TheGreatProgrammingJourney',
        'url_demo':   '',
        'data_inicio': '2024-02-01',
        'uc_codigo':   'LP2',
        'tecnologias': ['Java'],
    },
    {
        'titulo': 'Frontend Labs Collection',
        'descricao': (
            'Collection of frontend labs developed incrementally using HTML, CSS, and '
            'JavaScript, evolving towards modern frontend practices. Inclui dynamic data '
            'rendering, filters, sorting, user interaction e separação clara de estrutura, '
            'estilo e lógica.'
        ),
        'conceitos_aplicados': (
            'HTML semântico, CSS layouts, JavaScript DOM manipulation, separação de '
            'responsabilidades'
        ),
        'url_github': 'https://github.com/miguel-baptista07/FrontendLabsCollection',
        'url_demo':   '',
        'data_inicio': '2024-02-01',
        'uc_codigo':   'PW1',
        'tecnologias': ['HTML', 'CSS', 'JavaScript'],
    },
]


def load_tecnologias():
    print('Tecnologias:')
    tecs = {}
    for t in TECNOLOGIAS:
        obj, created = Tecnologia.objects.get_or_create(
            nome=t['nome'],
            defaults={
                'categoria':       t['categoria'],
                'nivel_interesse': t['nivel_interesse'],
                'url_oficial':     t['url_oficial'],
                'pontos_destaque': t['pontos_destaque'],
            }
        )
        status = 'CRIADA' if created else 'JÁ EXISTE'
        print(f'  [{status}] {obj.nome} ({obj.categoria})')
        tecs[obj.nome] = obj
    return tecs


def load_projetos(tecs):
    print('\nProjetos:')
    criados = existentes = erros = 0

    for p in PROJETOS:
        try:
            uc = UnidadeCurricular.objects.get(codigo=p['uc_codigo'])
        except UnidadeCurricular.DoesNotExist:
            print(f'  [ERRO] UC {p["uc_codigo"]} não encontrada — projeto "{p["titulo"][:50]}" ignorado')
            erros += 1
            continue

        try:
            obj, created = Projeto.objects.get_or_create(
                titulo=p['titulo'],
                defaults={
                    'descricao':          p['descricao'],
                    'conceitos_aplicados': p['conceitos_aplicados'],
                    'url_github':         p['url_github'],
                    'url_demo':           p['url_demo'],
                    'data_inicio':        p['data_inicio'],
                    'uc':                 uc,
                }
            )
            obj.tecnologias.set([tecs[n] for n in p['tecnologias']])

            status = 'CRIADO' if created else 'JÁ EXISTE'
            print(f'  [{status}] {obj.titulo[:60]}')
            print(f'           UC: {uc.codigo} | Tecnologias: {", ".join(p["tecnologias"])}')
            if created:
                criados += 1
            else:
                existentes += 1
        except Exception as e:
            erros += 1
            print(f'  [ERRO] {p["titulo"][:50]}: {e}')

    print(f'\n=== Resultado ===')
    print(f'Criados:     {criados}')
    print(f'Já existiam: {existentes}')
    print(f'Erros:       {erros}')
    print(f'Total:       {criados + existentes}')


def load_makingof():
    obj, created = MakingOf.objects.get_or_create(
        titulo='Modelação dos Projetos',
        entidade_relacionada='Projeto',
        defaults={
            'descricao': (
                'Carreguei 3 projetos realizados no âmbito das UCs de Programação Web e '
                'Linguagens de Programação II.'
            ),
            'decisoes_tomadas': (
                'Decidi relacionar cada projeto com a UC onde foi desenvolvido (FK) e com '
                'as tecnologias usadas (ManyToMany). Incluí url_github porque é fundamental '
                'para entrevistas de emprego. O campo conceitos_aplicados permite mostrar o '
                'que foi aprendido em cada UC.'
            ),
            'erros_correcoes': (
                'Inicialmente o modelo Projeto não tinha o campo conceitos_aplicados. Foi '
                'adicionado para cumprir o requisito mínimo de 5 atributos e por ser '
                'relevante para o portfolio.'
            ),
            'uso_ia': (
                'Utilizei o Claude para estruturar o script e sugerir as relações entre '
                'entidades. Os dados dos projetos são reais e foram desenvolvidos por mim.'
            ),
        }
    )
    status = 'CRIADO' if created else 'JÁ EXISTE'
    print(f'\nMaking Of: [{status}] {obj.titulo}')


if __name__ == '__main__':
    print('A carregar projetos e tecnologias...\n')
    tecs = load_tecnologias()
    load_projetos(tecs)
    load_makingof()
    print('\nConcluído.')
