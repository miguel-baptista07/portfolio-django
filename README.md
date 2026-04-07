# Portfolio Django — Miguel Baptista

Aplicação web Django que serve como portfolio académico e pessoal, desenvolvida no âmbito da UC de Programação Web da Licenciatura em Engenharia Informática da Universidade Lusófona.

## Como correr o projeto

### Localmente (Windows)
```bash
cd portfolio_project
C:\Users\migue\venv\Scripts\python.exe manage.py runserver
```
Aceder em: http://127.0.0.1:8000/admin

### No GitHub Codespace
```bash
pip install django pillow requests
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```
Aceder pelo separador PORTS → porta 8000

## Estrutura do Projeto
- `portfolio/` — App Django com os modelos
- `data/` — Scripts de carregamento de dados e ficheiros JSON
- `media/makingof/` — Fotografias do processo (DER desenhado à mão)
- `MAKING_OF.md` — Diário de bordo do processo de modelação

## Modelos
Licenciatura, UnidadeCurricular, Docente, Projeto, Tecnologia, TFC, Competencia, Formacao, Certificado (entidade extra), MakingOf

## Dados carregados
- 1 Licenciatura (LEI)
- 29 Unidades Curriculares com descrições da API Lusófona
- 3 Docentes reais com emails e URLs da Lusófona
- 3 Projetos com imagens
- 9 Tecnologias
- 35 TFCs
- 8 Competências
- 5 Formações + 1 Certificado

## Making Of
Documentação completa do processo em [MAKING_OF.md](MAKING_OF.md)
