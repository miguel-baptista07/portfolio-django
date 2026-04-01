#!/usr/bin/env python
"""Script para carregar TFCs a partir de um ficheiro JSON."""

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

from portfolio.models import TFC


def load_tfcs(json_path):
    """Carrega TFCs do ficheiro JSON para a base de dados."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            tfcs_data = json.load(f)
    except FileNotFoundError:
        print(f"Erro: Ficheiro '{json_path}' nao encontrado.")
        return
    except json.JSONDecodeError as e:
        print(f"Erro ao processar JSON: {e}")
        return

    print(f"A carregar {len(tfcs_data)} TFC(s)...")

    for tfc_data in tfcs_data:
        try:
            tfc, created = TFC.objects.get_or_create(
                titulo=tfc_data['titulo'],
                defaults={
                    'resumo': tfc_data.get('resumo', ''),
                    'autor': tfc_data.get('autor', ''),
                    'ano': tfc_data.get('ano', 2026),
                    'area': tfc_data.get('area', ''),
                    'classificacao': tfc_data.get('classificacao'),
                    'url_repositorio': tfc_data.get('url_repositorio', ''),
                }
            )
            if created:
                print(f"TFC criado: {tfc.titulo}")
            else:
                print(f"TFC atualizado: {tfc.titulo}")
        except KeyError as e:
            print(f"Erro: Campo obrigatorio em falta - {e}")
        except Exception as e:
            print(f"Erro ao processar TFC '{tfc_data.get('titulo', 'desconhecido')}': {e}")

    print("Carregamento concluido!")


if __name__ == '__main__':
    # Caminho relativo a partir da raiz do projeto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'tfcs.json')
    load_tfcs(json_path)
