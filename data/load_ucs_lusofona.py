#!/usr/bin/env python
"""Script para carregar UCs da Lusofona via API."""

import os
import sys
import json
import django

# Adicionar raiz do projeto ao PYTHONPATH
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.insert(0, project_root)

# Configurar ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

import requests
from portfolio.models import UnidadeCurricular


API_URL = "https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}


def load_ucs_lusofona():
    """Carrega UCs da API da Lusofona para a base de dados."""
    payload = {
        "language": "PT",
        "courseCode": 260,
        "schoolYear": "202526"
    }

    print(f"A chamar API Lusofona: {API_URL}")
    print(f"Payload: {payload}")

    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Erro: Timeout ao conectar a API.")
        return
    except requests.exceptions.ConnectionError as e:
        print(f"Erro de conexao: {e}")
        return
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisicao: {e}")
        return

    # Guardar JSON completo
    json_path = os.path.join(script_dir, 'curso_LEI.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, indent=2, ensure_ascii=False)
    print(f"JSON guardado em: {json_path}")

    data = response.json()

    # Extrair UCs do courseFlatPlan
    course_flat_plan = data.get('courseFlatPlan', [])
    if not course_flat_plan:
        print("Aviso: courseFlatPlan vazio ou nao encontrado.")
        return

    print(f"Encontradas {len(course_flat_plan)} UCs no courseFlatPlan.")

    criadas = 0
    atualizadas = 0
    erros = 0

    for uc_data in course_flat_plan:
        try:
            # Extrair campos da estrutura da API Lusofona
            # Usar curricularUnitCode ou curricularIUnitReadableCode como codigo
            codigo = uc_data.get('curricularIUnitReadableCode', '')
            if not codigo:
                codigo = str(uc_data.get('curricularUnitCode', ''))
            if not codigo:
                print(f"UC sem codigo, a ignorar: {uc_data.get('curricularUnitName', 'desconhecida')}")
                erros += 1
                continue

            nome = uc_data.get('curricularUnitName', '')
            ano_curricular = uc_data.get('curricularYear', 0)
            semestre_raw = uc_data.get('semester', '')
            # Converter semestre: "1º Semestre" -> 1, "2º Semestre" -> 2, "Semestral" -> 0
            semestre = 0
            if '1º' in semestre_raw or '1.' in semestre_raw:
                semestre = 1
            elif '2º' in semestre_raw or '2.' in semestre_raw:
                semestre = 2
            elif 'Semestral' in semestre_raw or 'Anual' in semestre_raw:
                semestre = 0

            ects = uc_data.get('ects', None)
            if ects is not None:
                try:
                    ects = float(ects)
                except (ValueError, TypeError):
                    ects = None

            duracao = uc_data.get('hrTotalContacto', '')
            # Construir URL se disponivel
            url = uc_data.get('curricularIUnitReadableCode', '')

            uc, created = UnidadeCurricular.objects.get_or_create(
                codigo=codigo,
                defaults={
                    'nome': nome,
                    'ano_curricular': ano_curricular,
                    'semestre': semestre,
                    'ects': ects,
                    'duracao': duracao,
                    'url': url,
                }
            )

            if created:
                print(f"UC criada: {nome} ({codigo})")
                criadas += 1
            else:
                # Atualizar se houver mudancas
                changed = False
                for field, value in [('nome', nome), ('ano_curricular', ano_curricular),
                                      ('semestre', semestre), ('ects', ects),
                                      ('duracao', duracao), ('url', url)]:
                    if getattr(uc, field) != value:
                        setattr(uc, field, value)
                        changed = True
                if changed:
                    uc.save()
                    print(f"UC atualizada: {nome} ({codigo})")
                    atualizadas += 1

        except Exception as e:
            print(f"Erro ao processar UC '{uc_data.get('name', 'desconhecida')}': {e}")
            erros += 1

    print(f"\nResumo: {criadas} criadas, {atualizadas} atualizadas, {erros} erros.")
    print("Carregamento concluido!")


if __name__ == '__main__':
    load_ucs_lusofona()
