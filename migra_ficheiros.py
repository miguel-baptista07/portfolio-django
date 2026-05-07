import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.core.files import File
from escola.models import Curso
from portfolio.models import Projeto, Tecnologia, Docente, UnidadeCurricular, MakingOf

MEDIA_ROOT = '/workspaces/portfolio-django/media'

def migra_campo(modelo, campo, pasta):
    for obj in modelo.objects.all():
        field = getattr(obj, campo)
        if field and field.name:
            local_path = os.path.join(MEDIA_ROOT, field.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    getattr(obj, campo).save(os.path.basename(local_path), File(f), save=True)
                print(f'[OK] {modelo.__name__}: {obj}')
            else:
                print(f'[NAO EXISTE] {local_path}')

migra_campo(Curso, 'imagem', 'cursos')
migra_campo(Projeto, 'imagem', 'projetos')
migra_campo(Tecnologia, 'logo', 'tecnologias')
migra_campo(Docente, 'foto', 'docentes')
migra_campo(UnidadeCurricular, 'imagem', 'ucs')
migra_campo(MakingOf, 'foto_caderno', 'makingof')
