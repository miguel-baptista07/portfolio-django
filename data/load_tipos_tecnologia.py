import os
import sys
import django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import TipoTecnologia, Tecnologia

# 1. Criar tipos
tipos_nomes = ["Frontend", "Backend", "Base de Dados", "Storage", "Outros"]
tipos = {}
for nome in tipos_nomes:
    obj, created = TipoTecnologia.objects.get_or_create(nome=nome)
    tipos[nome] = obj
    print(f"{'Criado' if created else 'Já existe'}: TipoTecnologia '{nome}'")

# 2. Associar tecnologias aos tipos
associacoes = {
    "Frontend":      ["React", "Next.js", "TypeScript", "Tailwind CSS", "HTML", "CSS", "JavaScript", "SWR"],
    "Backend":       ["Java", "Python", "Django"],
    "Outros":        ["Git"],
}

atualizadas = 0
nao_encontradas = []

for tipo_nome, nomes_tec in associacoes.items():
    tipo = tipos[tipo_nome]
    for nome in nomes_tec:
        try:
            tec = Tecnologia.objects.get(nome=nome)
            tec.tipo = tipo
            tec.save()
            print(f"  Associado: '{nome}' -> {tipo_nome}")
            atualizadas += 1
        except Tecnologia.DoesNotExist:
            nao_encontradas.append(nome)
            print(f"  Não encontrada: '{nome}'")

# 3. Resumo
print(f"\nTipos criados/verificados: {len(tipos_nomes)}")
print(f"Tecnologias associadas:    {atualizadas}")
if nao_encontradas:
    print(f"Tecnologias não encontradas ({len(nao_encontradas)}): {', '.join(nao_encontradas)}")
