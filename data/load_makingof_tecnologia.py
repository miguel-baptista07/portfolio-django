import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import MakingOf

if __name__ == '__main__':
    obj, created = MakingOf.objects.get_or_create(
        titulo='Modelação das Tecnologias',
        entidade_relacionada='Tecnologia',
        defaults={
            'descricao': (
                'Carreguei 9 tecnologias usadas nos meus projetos: React, Next.js, '
                'TypeScript, Tailwind CSS, SWR, Java, HTML, CSS e JavaScript.'
            ),
            'decisoes_tomadas': (
                'Decidi incluir logo, url_oficial, categoria, nivel_interesse e '
                'pontos_destaque. O campo nivel_interesse permite mostrar as minhas '
                'preferências tecnológicas. A categoria agrupa as tecnologias por tipo '
                '(Frontend, Linguagem, etc.). A relação com Projeto é ManyToMany porque '
                'um projeto pode usar várias tecnologias e uma tecnologia pode ser usada '
                'em vários projetos.'
            ),
            'erros_correcoes': (
                'Inicialmente o modelo não tinha o campo pontos_destaque. Foi adicionado '
                'para cumprir o requisito de incluir informação que destaque os aspetos '
                'mais relevantes de cada tecnologia.'
            ),
            'uso_ia': (
                'Utilizei o Claude para sugerir os atributos do modelo e estruturar o '
                'script. As tecnologias e os níveis de interesse foram definidos por mim '
                'com base na minha experiência real.'
            ),
        }
    )
    status = 'CRIADO' if created else 'JÁ EXISTE'
    print(f'[{status}] {obj.titulo} (entidade: {obj.entidade_relacionada})')
