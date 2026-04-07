import requests
import django
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from portfolio.models import UnidadeCurricular

ucs = UnidadeCurricular.objects.filter(descricao='')
print(f'UCs sem descricao: {ucs.count()}')

for uc in ucs:
    try:
        url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
        payload = {'language': 'PT', 'curricularIUnitReadableCode': uc.codigo}
        headers = {'content-type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        descricao = data.get('description', '') or data.get('objectives', '') or ''
        if descricao:
            uc.descricao = descricao[:1000]
            uc.save()
            print(f'  [OK] {uc.codigo} - {uc.nome}')
        else:
            print(f'  [VAZIO] {uc.codigo} - {uc.nome}')
    except Exception as e:
        print(f'  [ERRO] {uc.codigo}: {e}')
