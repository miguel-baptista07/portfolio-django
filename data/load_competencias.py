import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import Competencia, Tecnologia, Projeto, MakingOf

COMPETENCIAS = [
    {
        'nome': 'Programação em Java',
        'nivel': 'Intermédio',
        'categoria': 'Linguagens',
        'descricao': (
            'Desenvolvimento de aplicações Java com foco em OOP, herança e polimorfismo. '
            'Usado em projetos académicos e open source (Spring Boot, Maven).'
        ),
        'tecnologias': ['Java'],
        'projetos': ['The Great Programming Journey'],
    },
    {
        'nome': 'Programação em Python',
        'nivel': 'Intermédio',
        'categoria': 'Linguagens',
        'descricao': (
            'Desenvolvimento de ferramentas de cibersegurança em Python: packet sniffer, '
            'port scanner e hash cracker usando raw sockets e criptografia.'
        ),
        'tecnologias': [],
        'projetos': [],
    },
    {
        'nome': 'Desenvolvimento Web Frontend',
        'nivel': 'Intermédio',
        'categoria': 'Frameworks & Libraries',
        'descricao': (
            'Criação de aplicações web modernas com React, Next.js, TypeScript e Tailwind '
            'CSS. Experiência com routing dinâmico, gestão de estado e data fetching.'
        ),
        'tecnologias': ['React', 'Next.js', 'TypeScript', 'Tailwind CSS', 'JavaScript', 'HTML', 'CSS'],
        'projetos': [
            'React & Next.js — Frontend Labs & E-Commerce Platform',
            'Frontend Labs Collection',
        ],
    },
    {
        'nome': 'Controlo de Versões com Git',
        'nivel': 'Intermédio',
        'categoria': 'Ferramentas',
        'descricao': (
            'Utilização profissional de Git e GitHub: branching, pull requests, code review, '
            'issue tracking e workflows ágeis. Aplicado em contribuições open source.'
        ),
        'tecnologias': [],
        'projetos': [],
    },
    {
        'nome': 'Cibersegurança',
        'nivel': 'Iniciante',
        'categoria': 'Área Técnica',
        'descricao': (
            'Conhecimentos práticos de cibersegurança: análise de tráfego de rede, scanning '
            'de portas, criptografia SHA1 e técnicas de ataque por dicionário.'
        ),
        'tecnologias': [],
        'projetos': [],
    },
    {
        'nome': 'Orientação a Objetos (OOP)',
        'nivel': 'Intermédio',
        'categoria': 'Conceitos CS',
        'descricao': (
            'Aplicação de princípios OOP: herança, polimorfismo, encapsulamento e MVC. '
            'Usado em Java e projetos académicos.'
        ),
        'tecnologias': ['Java'],
        'projetos': ['The Great Programming Journey'],
    },
    {
        'nome': 'Contribuição Open Source',
        'nivel': 'Intermédio',
        'categoria': 'Práticas de Desenvolvimento',
        'descricao': (
            'Contribuição para repositórios open source com workflow profissional: debugging, '
            'testes unitários e de integração, PRs e code review em codebases multi-linguagem '
            '(Java, Kotlin, Spring Boot, Django).'
        ),
        'tecnologias': ['Java'],
        'projetos': [],
    },
    {
        'nome': 'Liderança e Trabalho em Equipa',
        'nivel': 'Intermédio',
        'categoria': 'Soft Skills',
        'descricao': (
            'Capacidade de liderança em situações de pressão e suporte ao desempenho de '
            'equipa. Demonstrado no NEDI e como CGI Campus Ambassador.'
        ),
        'tecnologias': [],
        'projetos': [],
    },
]


def resolve_tecnologias(nomes):
    result = []
    for nome in nomes:
        try:
            result.append(Tecnologia.objects.get(nome=nome))
        except Tecnologia.DoesNotExist:
            print(f'    [AVISO] Tecnologia "{nome}" não encontrada — ignorada')
    return result


def resolve_projetos(titulos):
    result = []
    for titulo in titulos:
        try:
            result.append(Projeto.objects.get(titulo=titulo))
        except Projeto.DoesNotExist:
            print(f'    [AVISO] Projeto "{titulo[:50]}" não encontrado — ignorado')
    return result


def load_competencias():
    criadas = existentes = erros = 0

    for c in COMPETENCIAS:
        try:
            obj, created = Competencia.objects.get_or_create(
                nome=c['nome'],
                defaults={
                    'nivel':     c['nivel'],
                    'categoria': c['categoria'],
                    'descricao': c['descricao'],
                }
            )
            obj.tecnologias.set(resolve_tecnologias(c['tecnologias']))
            obj.projetos.set(resolve_projetos(c['projetos']))

            status = 'CRIADA' if created else 'JÁ EXISTE'
            print(f'  [{status}] {obj.nome} ({obj.nivel} | {obj.categoria})')
            if created:
                criadas += 1
            else:
                existentes += 1
        except Exception as e:
            erros += 1
            print(f'  [ERRO] {c["nome"]}: {e}')

    print(f'\n=== Resultado ===')
    print(f'Criadas:     {criadas}')
    print(f'Já existiam: {existentes}')
    print(f'Erros:       {erros}')
    print(f'Total:       {criadas + existentes}')


def load_makingof():
    obj, created = MakingOf.objects.get_or_create(
        titulo='Modelação das Competências',
        entidade_relacionada='Competencia',
        defaults={
            'descricao': (
                'Carreguei 8 competências retiradas do meu CV, organizadas por categoria: '
                'Linguagens, Frameworks, Ferramentas, Conceitos CS, Área Técnica, Práticas '
                'de Desenvolvimento e Soft Skills.'
            ),
            'decisoes_tomadas': (
                'Decidi relacionar as competências com as tecnologias e projetos já '
                'existentes para mostrar evidência concreta de cada competência. O campo '
                'nivel segue a escala Iniciante/Intermédio/Avançado, comum em CVs.'
            ),
            'erros_correcoes': (
                'Algumas tecnologias referenciadas no CV (Python, Kotlin, Spring Boot) ainda '
                'não estavam na BD como tecnologias. Foram adicionadas as relações apenas '
                'com as tecnologias já existentes.'
            ),
            'uso_ia': (
                'Utilizei o Claude para extrair as competências do meu CV e estruturá-las no '
                'formato do modelo Django. A seleção e descrição final foi revista por mim.'
            ),
        }
    )
    status = 'CRIADO' if created else 'JÁ EXISTE'
    print(f'\nMaking Of: [{status}] {obj.titulo}')


if __name__ == '__main__':
    print('A carregar competências...\n')
    load_competencias()
    load_makingof()
    print('\nConcluído.')
