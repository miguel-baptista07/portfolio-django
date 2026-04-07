import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import Licenciatura, MakingOf


def load_licenciaturas():
    obj, created = Licenciatura.objects.get_or_create(
        sigla='LEI',
        defaults={
            'nome': 'Engenharia Informática',
            'grau': 'Licenciatura',
            'ects': 180,
            'duracao_anos': 3,
            'url_lusofona': 'https://www.ulusofona.pt/licenciatura/engenharia-informatica',
            'descricao': (
                'O curso de licenciatura em Engenharia Informática da Universidade Lusófona '
                'forma licenciados capazes de assumir posições de destaque em projetos de '
                'engenharia informática ou equipas de desenvolvimento e consultadoria. Os '
                'estudantes obtêm competências adequadas à conceção, realização e manutenção '
                'de sistemas informáticos, programação de aplicações e de sistemas, desenho '
                'de arquiteturas de computação e comunicações, gestão de sistemas de '
                'informação e de conhecimento.'
            ),
        }
    )
    status = 'CRIADO' if created else 'JÁ EXISTE'
    print(f'  [{status}] Licenciatura: {obj.nome} ({obj.sigla})')
    return obj


def load_makingof_licenciatura(licenciatura):
    obj, created = MakingOf.objects.get_or_create(
        titulo='Modelação da entidade Licenciatura',
        entidade_relacionada='Licenciatura',
        defaults={
            'descricao': (
                'Modelei a entidade Licenciatura com base na informação disponível no site '
                'da Lusófona sobre o curso de Engenharia Informática.'
            ),
            'decisoes_tomadas': (
                'Decidi incluir nome, sigla, grau, ects, duracao_anos, url_lusofona e '
                'descricao. Não incluí campos como coordenador por não serem relevantes '
                'para um portfolio pessoal. O campo url_lusofona é importante para '
                'referenciar a fonte oficial.'
            ),
            'erros_correcoes': (
                'Inicialmente o modelo não tinha os campos grau e duracao_anos. Foram '
                'adicionados depois de consultar o site da Lusófona.'
            ),
            'uso_ia': (
                'Utilizei o Claude para sugerir atributos relevantes com base no enunciado '
                'e no site da Lusófona. A IA ajudou a estruturar o DER e a gerar os prompts '
                'para o Claude Code. As decisões finais foram minhas.'
            ),
        }
    )
    status = 'CRIADO' if created else 'JÁ EXISTE'
    print(f'  [{status}] MakingOf: {obj.titulo}')
    return obj


if __name__ == '__main__':
    print('A carregar dados iniciais...\n')

    print('Licenciaturas:')
    lei = load_licenciaturas()

    print('\nMaking Of:')
    load_makingof_licenciatura(lei)

    print('\nConcluído.')
