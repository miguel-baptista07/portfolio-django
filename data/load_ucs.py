import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular, MakingOf

UCS = [
    # 1º Ano - 1º Semestre
    {'codigo': 'FP1',  'nome': 'Fundamentos de Física',              'ano': 1, 'semestre': 1, 'ects': 6},
    {'codigo': 'FPR',  'nome': 'Fundamentos de Programação',         'ano': 1, 'semestre': 1, 'ects': 6},
    {'codigo': 'MD1',  'nome': 'Matemática Discreta',                'ano': 1, 'semestre': 1, 'ects': 6},
    {'codigo': 'MAT1', 'nome': 'Matemática I',                       'ano': 1, 'semestre': 1, 'ects': 6},
    {'codigo': 'SD1',  'nome': 'Sistemas Digitais',                  'ano': 1, 'semestre': 1, 'ects': 6},
    # 1º Ano - 2º Semestre
    {'codigo': 'AL1',  'nome': 'Álgebra Linear',                     'ano': 1, 'semestre': 2, 'ects': 6},
    {'codigo': 'AED',  'nome': 'Algoritmia e Estruturas de Dados',   'ano': 1, 'semestre': 2, 'ects': 6},
    {'codigo': 'AC1',  'nome': 'Arquitetura de Computadores',        'ano': 1, 'semestre': 2, 'ects': 6},
    {'codigo': 'CB1',  'nome': 'Competências Comportamentais',       'ano': 1, 'semestre': 2, 'ects': 6},
    {'codigo': 'LP1',  'nome': 'Linguagens de Programação I',        'ano': 1, 'semestre': 2, 'ects': 6},
    {'codigo': 'MAT2', 'nome': 'Matemática II',                      'ano': 1, 'semestre': 2, 'ects': 6},
    # 2º Ano - 1º Semestre
    {'codigo': 'AAC',  'nome': 'Arquiteturas Avançadas de Computadores', 'ano': 2, 'semestre': 1, 'ects': 6},
    {'codigo': 'BD1',  'nome': 'Bases de Dados',                    'ano': 2, 'semestre': 1, 'ects': 6},
    {'codigo': 'LP2',  'nome': 'Linguagens de Programação II',       'ano': 2, 'semestre': 1, 'ects': 6},
    {'codigo': 'PE1',  'nome': 'Probabilidades e Estatística',       'ano': 2, 'semestre': 1, 'ects': 6},
    {'codigo': 'SO1',  'nome': 'Sistemas Operativos',                'ano': 2, 'semestre': 1, 'ects': 6},
    # 2º Ano - 2º Semestre
    {'codigo': 'ERT',  'nome': 'Engenharia de Requisitos e Testes',  'ano': 2, 'semestre': 2, 'ects': 6},
    {'codigo': 'PI1',  'nome': 'Processamento de Imagem',            'ano': 2, 'semestre': 2, 'ects': 6},
    {'codigo': 'PW1',  'nome': 'Programação Web',                    'ano': 2, 'semestre': 2, 'ects': 6},
    {'codigo': 'RC1',  'nome': 'Redes de Computadores',              'ano': 2, 'semestre': 2, 'ects': 6},
    {'codigo': 'SSD',  'nome': 'Sistemas de Suporte à Decisão',      'ano': 2, 'semestre': 2, 'ects': 6},
    # 3º Ano - 1º Semestre
    {'codigo': 'CD1',  'nome': 'Computação Distribuída',             'ano': 3, 'semestre': 1, 'ects': 6},
    {'codigo': 'DS1',  'nome': 'Data Science',                       'ano': 3, 'semestre': 1, 'ects': 6},
    {'codigo': 'ES1',  'nome': 'Engenharia de Software',             'ano': 3, 'semestre': 1, 'ects': 6},
    {'codigo': 'IHM',  'nome': 'Interação Humano-Máquina',           'ano': 3, 'semestre': 1, 'ects': 6},
    # 3º Ano - 2º Semestre
    {'codigo': 'CM1',  'nome': 'Computação Móvel',                   'ano': 3, 'semestre': 2, 'ects': 6},
    {'codigo': 'IA1',  'nome': 'Inteligência Artificial',            'ano': 3, 'semestre': 2, 'ects': 6},
    {'codigo': 'SI1',  'nome': 'Segurança Informática',              'ano': 3, 'semestre': 2, 'ects': 6},
    {'codigo': 'SIC',  'nome': 'Sistemas de Informação na Nuvem',    'ano': 3, 'semestre': 2, 'ects': 6},
]


def load_ucs():
    lei = Licenciatura.objects.get(sigla='LEI')
    print(f'Licenciatura encontrada: {lei.nome} ({lei.sigla})\n')

    criadas = 0
    existentes = 0
    erros = 0

    for uc_data in UCS:
        try:
            uc, created = UnidadeCurricular.objects.get_or_create(
                codigo=uc_data['codigo'],
                defaults={
                    'nome': uc_data['nome'],
                    'ano': uc_data['ano'],
                    'semestre': uc_data['semestre'],
                    'ects': uc_data['ects'],
                    'licenciatura': lei,
                }
            )
            if not created and uc.licenciatura != lei:
                uc.licenciatura = lei
                uc.save()

            status = 'CRIADA' if created else 'JÁ EXISTE'
            print(f'  [{status}] {uc.codigo} - {uc.nome} ({uc.ano}º ano, {uc.semestre}º sem)')
            if created:
                criadas += 1
            else:
                existentes += 1
        except Exception as e:
            erros += 1
            print(f'  [ERRO] {uc_data["codigo"]} - {uc_data["nome"]}: {e}')

    print(f'\n=== Resultado ===')
    print(f'Criadas:     {criadas}')
    print(f'Já existiam: {existentes}')
    print(f'Erros:       {erros}')
    print(f'Total:       {criadas + existentes}')


def load_makingof():
    obj, created = MakingOf.objects.get_or_create(
        titulo='Modelação das Unidades Curriculares',
        entidade_relacionada='UnidadeCurricular',
        defaults={
            'descricao': (
                'Carreguei todas as 28 UCs do curso LEI organizadas por ano e semestre.'
            ),
            'decisoes_tomadas': (
                'Decidi incluir codigo, nome, ano, semestre e ects como atributos principais. '
                'A imagem foi deixada para adicionar manualmente no admin. A relação com '
                'Docente é ManyToMany porque uma UC pode ter vários docentes e um docente '
                'pode lecionar várias UCs. A relação com Licenciatura é FK porque cada UC '
                'pertence a uma licenciatura.'
            ),
            'erros_correcoes': (
                'Os códigos das UCs foram definidos manualmente pois a API da Lusófona usa '
                'códigos diferentes. Ajustado após verificação.'
            ),
            'uso_ia': (
                'Utilizei o Claude para estruturar o script de carregamento e definir os '
                'atributos do modelo. A lista de UCs foi retirada do site da Lusófona.'
            ),
        }
    )
    status = 'CRIADO' if created else 'JÁ EXISTE'
    print(f'\nMaking Of: [{status}] {obj.titulo}')


if __name__ == '__main__':
    print('A carregar Unidades Curriculares do curso LEI...\n')
    load_ucs()
    load_makingof()
    print('\nConcluído.')
