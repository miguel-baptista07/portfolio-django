# Portfolio Project

Projeto de portfólio Django para gestão de trabalhos finais de curso (TFC), unidades curriculares e making-of.

## Tecnologias

- **Python 3.13**
- **Django 5.2**
- **SQLite** (desenvolvimento) / **MySQL** (produção)
- **requests** (integração com API externa)

## Funcionalidades

- Gestão de TFCs (Trabalhos Finais de Curso)
- Gestão de Unidades Curriculares (importação via API da Lusófona)
- Gestão de Making-of
- Admin Django configurado com listagem e pesquisa

## Instalação Local

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd portfolio_project
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Aplicar migrações

```bash
python manage.py migrate
```

### 6. Criar superutilizador (opcional)

```bash
python manage.py createsuperuser
```

### 7. Correr o servidor de desenvolvimento

```bash
python manage.py runserver
```

O projeto estará disponível em: http://127.0.0.1:8000/

## Scripts de Carregamento de Dados

### Carregar TFCs de exemplo

```bash
python data/load_tfcs.py
```

### Carregar UCs da API da Lusófona

```bash
python data/load_ucs_lusofona.py
```

## Estrutura do Projeto

```
portfolio_project/
├── portfolio/          # App principal
│   ├── models.py       # Modelos: TFC, UnidadeCurricular, MakingOf
│   ├── admin.py        # Registo no admin
│   └── migrations/     # Migrações da base de dados
├── data/               # Scripts e dados de carregamento
│   ├── load_tfcs.py
│   ├── load_ucs_lusofona.py
│   ├── tfcs.json
│   └── curso_LEI.json
├── manage.py
├── requirements.txt
└── README.md
```

## Licença

MIT
