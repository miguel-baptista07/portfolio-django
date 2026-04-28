# Portfolio Django — Miguel Baptista

Aplicação web Django que serve como portfolio académico e pessoal, desenvolvida no âmbito da UC de Programação Web da Licenciatura em Engenharia Informática da Universidade Lusófona.

## Como correr o projeto

### Instalar dependências
```bash
pip install django pillow requests django-markdownify whitenoise
```

### Migrações
```bash
python manage.py migrate
```

### Criar superuser
```bash
python manage.py createsuperuser
```
Credenciais sugeridas: username `migue`, password `12345`

### Popular a base de dados
```bash
python data/load_initial_data.py && python data/load_ucs.py && python data/load_tfcs.py && python data/load_projetos.py && python data/load_competencias.py && python data/load_formacoes.py && python data/load_docentes_ucs.py && python data/load_tipos_tecnologia.py
```

### Popular a app Escola
```bash
python manage.py loaddata data/load_escola_fixture.json
```

### Correr o servidor
```bash
python manage.py runserver 0.0.0.0:8000
```

## Estrutura do Projeto
- `portfolio/` — App Django com os modelos
- `escola/` — App Django de exemplo com modelos Professor/Aluno/Curso
- `data/` — Scripts de carregamento de dados e ficheiros JSON
- `media/makingof/` — Fotografias do processo (DER desenhado à mão)
- `MAKING_OF.md` — Diário de bordo do processo de modelação

## Modelos
Licenciatura, UnidadeCurricular, Docente, Projeto, Tecnologia, TipoTecnologia, TFC, Competencia, Formacao, Certificado (entidade extra), MakingOf

## Dados carregados
- 1 Licenciatura (LEI)
- 29 Unidades Curriculares com descrições da API Lusófona
- 3 Docentes reais com emails e URLs da Lusófona
- 3 Projetos com imagens
- 12 Tecnologias organizadas por tipo
- 35 TFCs
- 8 Competências
- 5 Formações + 1 Certificado

## Making Of
Documentação completa do processo em [MAKING_OF.md](MAKING_OF.md)
