import os
import sys
import json
import requests
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import UnidadeCurricular

API_URL = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
HEADERS = {'content-type': 'application/json'}

JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'curso_LEI.json')

with open(JSON_PATH, encoding='utf-8') as f:
    data = json.load(f)

plan = data.get('courseFlatPlan', [])
print(f'UCs no JSON: {len(plan)}\n')

atualizadas = vazias = erros = 0

for entry in plan:
    api_code = entry.get('curricularIUnitReadableCode', '')
    nome_json = entry.get('curricularUnitName', '').strip()

    if not api_code or not nome_json:
        continue

    # Match pelo nome na BD
    try:
        uc = UnidadeCurricular.objects.get(nome__iexact=nome_json)
    except UnidadeCurricular.DoesNotExist:
        print(f'  [SEM MATCH] "{nome_json}" — não encontrada na BD')
        erros += 1
        continue
    except UnidadeCurricular.MultipleObjectsReturned:
        print(f'  [DUPLICADO] "{nome_json}" — múltiplos resultados')
        erros += 1
        continue

    # Pedido à API com o código real
    try:
        response = requests.post(
            API_URL,
            json={'language': 'PT', 'curricularIUnitReadableCode': api_code},
            headers=HEADERS,
            timeout=10,
        )
        resp_data = response.json()
        descricao = (
            resp_data.get('description', '') or
            resp_data.get('objectives', '') or
            resp_data.get('syllabus', '') or
            ''
        )
        if descricao:
            uc.descricao = descricao[:1000]
            uc.save()
            print(f'  [OK]    {uc.codigo} - {uc.nome[:50]}')
            atualizadas += 1
        else:
            print(f'  [VAZIO] {uc.codigo} - {uc.nome[:50]} (api_code={api_code})')
            vazias += 1
    except Exception as e:
        print(f'  [ERRO]  {uc.codigo} - {uc.nome[:50]}: {e}')
        erros += 1

print(f'\n=== Resultado ===')
print(f'Atualizadas: {atualizadas}')
print(f'Vazias:      {vazias}')
print(f'Erros:       {erros}')
