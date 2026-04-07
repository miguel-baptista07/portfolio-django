# Making Of — Portfolio Django
**Autor:** Miguel Baptista  
**Curso:** Licenciatura em Engenharia Informática — Universidade Lusófona  
**UC:** Programação Web  
**Data:** Abril 2026  

---

## Introdução

Este documento é o diário de bordo do processo de modelação e desenvolvimento do portfolio académico em Django. Regista todas as decisões tomadas, erros encontrados, correções aplicadas e justificações das escolhas de modelação. O objetivo é documentar não só o resultado final, mas o processo de pensamento que levou até ele.

O projeto consiste numa aplicação web Django que serve como portfolio académico e pessoal, reunindo informação sobre a licenciatura, unidades curriculares, projetos, tecnologias, competências e formações.

---

## Diagrama Entidade-Relação (DER)

O DER foi desenhado à mão no caderno antes de iniciar a implementação. A fotografia encontra-se em `media/makingof/DER- portfolio.jpeg`.

---

## Decisões de Modelação por Entidade

### 1. Licenciatura
**Decisão 1 — Incluir `sigla`:** A sigla (LEI) é usada frequentemente em referências internas. Facilita pesquisas e filtragens no admin.  
**Decisão 2 — Incluir `url_lusofona`:** Permite ao visitante verificar a fonte oficial e aceder a informação atualizada.  
**Decisão 3 — Não incluir `coordenador`:** Não é relevante para um portfolio pessoal.

### 2. Unidade Curricular
**Decisão 1 — Incluir `codigo`:** Único e permite identificar rapidamente cada disciplina e associar projetos à UC correspondente.  
**Decisão 2 — Relação ManyToMany com Docente:** Uma UC pode ter vários docentes e um docente pode lecionar várias UCs.  
**Decisão 3 — Relação ManyToMany com Tecnologia:** Permite mostrar em que contexto cada tecnologia foi aprendida.

### 3. Docente
**Decisão 1 — Incluir `url_lusofona`:** O enunciado especifica explicitamente a ligação à página pessoal no site da Lusófona.  
**Decisão 2 — Incluir `foto`:** Humaniza o portfolio. Campo opcional para não obrigar a ter foto de todos os docentes.

### 4. Projeto
**Decisão 1 — Incluir `url_github`:** O enunciado destaca que é muito importante para entrevistas de emprego.  
**Decisão 2 — Incluir `conceitos_aplicados`:** Mostra o que foi aprendido em cada projeto — o que um recrutador quer saber.  
**Decisão 3 — Incluir `data_inicio` e `data_fim`:** Permitem ordenar cronologicamente e mostrar a evolução ao longo do curso.  
**Decisão 4 — FK para UnidadeCurricular:** Contextualiza o projeto académico e mostra a progressão ao longo do curso.

### 5. Tecnologia
**Decisão 1 — Incluir `nivel_interesse` (1-5):** Permite mostrar as tecnologias favoritas de forma simples e visual.  
**Decisão 2 — Incluir `categoria`:** Agrupa tecnologias por tipo (Linguagem, Frontend, etc.) para facilitar a navegação.  
**Decisão 3 — Incluir `pontos_destaque`:** Permite destacar o que foi mais marcante na aprendizagem de cada tecnologia.

### 6. TFC
**Decisão 1 — `licenciatura_nome` como CharField em vez de FK:** O JSON real contém apenas texto sem correspondência com IDs da BD. Evita erros de integridade.  
**Decisão 2 — Incluir `classificacao` (1-5):** Permite destacar os TFCs de maior interesse conforme pedido no enunciado.

### 7. Competência
**Decisão 1 — Incluir `nivel` (Iniciante/Intermédio/Avançado):** Escala padrão em CVs, reconhecida no mercado de trabalho.  
**Decisão 2 — Relação ManyToMany com Tecnologia e Projeto:** Mostra evidência concreta de cada competência.

### 8. Formação
**Decisão 1 — Usar `data_inicio` e `data_fim`:** Permite ordenação cronológica automática e filtrar formações em curso.  
**Decisão 2 — Incluir `tipo`:** Diferencia entre Ensino Superior, Certificação Online, Experiência Profissional e Associação Estudantil.

### 9. Certificado ⭐ (Entidade Extra)
**Justificação:** Separei o Certificado da Formação porque nem todas as formações geram um certificado com código verificável. Segue o princípio da normalização — evita campos nulos em muitas formações.  
**Decisão 1 — Separar de Formação:** Uma formação pode não ter certificado (ex: participação no NEDI).  
**Decisão 2 — FK com Formação:** Um certificado pertence a uma formação específica.

### 10. MakingOf 🔴
**Decisão 1 — `entidade_relacionada` como CharField:** Simplifica o modelo em vez de criar FKs separadas para cada entidade.  
**Decisão 2 — Incluir `uso_ia`:** O enunciado especifica explicitamente que o uso de IA deve ser documentado.

---

## Erros Encontrados e Correções

| # | Erro | Correção |
|---|------|----------|
| 1 | Modelo TFC com campos que não existiam no JSON real | Análise do JSON e recriação do modelo com campos corretos |
| 2 | Modelos não guardados corretamente após prompts iniciais | Recriação de todos os modelos conforme o DER |
| 3 | Campo `decisoes_tomadas` sem `blank=True` impediu migração | Adicionado `default=''` temporariamente |
| 4 | Nomes dos docentes sem acentos por encoding no Windows | Script corrigido com `io.TextIOWrapper` e `encoding='utf-8'` |
| 5 | `uso_ia` removido do MakingOf por engano | Campo reposto após revisão do enunciado |
| 6 | Push feito para o repositório errado | Remote corrigido e push para repositório correto |

---

## Uso de Inteligência Artificial

Utilizei o **Claude** (Anthropic) como ferramenta de apoio. O uso foi transparente e controlado:

**Como foi utilizado:** Geração de scripts de carregamento de dados, sugestão de atributos para cada entidade, resolução de erros técnicos e estruturação do DER.

**O que foi decidido por mim:** Quais atributos incluir, a escolha da entidade extra (Certificado), os dados reais inseridos, o DER desenhado à mão e todas as decisões de modelação justificadas neste documento.

---

*Miguel Baptista — Abril 2026*
