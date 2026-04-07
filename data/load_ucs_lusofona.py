import os
import sys
import json
import django

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
sys.path.insert(0, project_root)

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
    payload = {
        "language": "PT",
        "courseCode": 260,
        "schoolYear": "202526"
    }

    print(f"A chamar API Lusofona: {API_URL}")

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

    json_path = os.path.join(script_dir, 'curso_LEI.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, indent=2, ensure_ascii=False)
    print(f"JSON guardado em: {json_path}")

    data = response.json()
    course_flat_plan = data.get('courseFlatPlan', [])
    if not course_flat_plan:
        print("Aviso: courseFlatPlan vazio ou nao encontrado.")
        return

    print(f"Encontradas {len(course_flat_plan)} UCs.")

    criadas = atualizadas = erros = 0

    for uc_data in course_flat_plan:
        try:
            codigo = uc_data.get('curricularIUnitReadableCode', '')
            if not codigo:
                codigo = str(uc_data.get('curricularUnitCode', ''))
            if not codigo:
                erros += 1
                continue

            nome = uc_data.get('curricularUnitName', '')
            ano_curricular = uc_data.get('curricularYear', 0)

            semestre_raw = uc_data.get('semester', '')
            semestre = 0
            if '1º' in semestre_raw or '1.' in semestre_raw:
                semestre = 1
            elif '2º' in semestre_raw or '2.' in semestre_raw:
                semestre = 2

            ects = uc_data.get('ects', None)
            if ects is not None:
                try:
                    ects = float(ects)
                except (ValueError, TypeError):
                    ects = None

            duracao = uc_data.get('hrTotalContacto', '')
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
            print(f"Erro ao processar UC: {e}")
            erros += 1

    print(f"\nResumo: {criadas} criadas, {atualizadas} atualizadas, {erros} erros.")


if __name__ == '__main__':
    load_ucs_lusofona()
