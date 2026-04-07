import os
import sys
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.insert(0, project_root)

django.setup()

from portfolio.models import TFC

JSON_PATH = os.path.join(script_dir, 'tfcs_deisi_2024_2025.json')

with open(JSON_PATH, encoding='utf-8') as f:
    data = json.load(f)

tfcs = data.get('tfcs', [])
print(f"Total de TFCs no ficheiro: {len(tfcs)}")

criados = 0
atualizados = 0
erros = 0

for entry in tfcs:
    try:
        titulo = entry.get('titulo', '').strip()
        autor = ', '.join(entry.get('autores', []))
        orientador = ', '.join(entry.get('orientadores', []))
        licenciatura_nome = ', '.join(entry.get('licenciaturas', []))
        ano = int(entry.get('ano', 0))
        email = entry.get('email', '') or ''
        url_pdf = entry.get('link_pdf') or None
        url_imagem = entry.get('imagem') or None
        resumo = entry.get('sumario', '') or ''
        classificacao = int(entry.get('rating', 3))
        classificacao = max(1, min(5, classificacao))

        obj, created = TFC.objects.get_or_create(
            titulo=titulo,
            autor=autor,
            defaults={
                'orientador': orientador,
                'licenciatura_nome': licenciatura_nome,
                'ano': ano,
                'email': email,
                'url_pdf': url_pdf,
                'url_imagem': url_imagem,
                'resumo': resumo,
                'classificacao': classificacao,
            }
        )

        if created:
            criados += 1
            print(f"  [CRIADO] {titulo[:70]}")
        else:
            atualizados += 1
            print(f"  [JA EXISTE] {titulo[:70]}")

    except Exception as e:
        erros += 1
        print(f"  [ERRO] {entry.get('titulo', '?')[:70]} -> {e}")

print(f"\n=== Resultado ===")
print(f"Criados:     {criados}")
print(f"Ja existiam: {atualizados}")
print(f"Erros:       {erros}")
print(f"Total:       {criados + atualizados}")
