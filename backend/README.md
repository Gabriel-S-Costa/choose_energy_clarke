# Choose Energy Clarke - Backend

Bem-vindo ao repositório backend do **Desafio Clarke Energia**. Esta aplicação é uma API RESTful construída com Python fornecendo funcionalidades para gerenciamento e busca de fornecedores de energia (suppliers).

## 🚀 Tecnologias e Dependências

O projeto foi construído utilizando as seguintes ferramentas do ecossistema Python:

- **Linguagem**: [Python 3.12+](https://www.python.org/)
- **Framework Web**: [FastAPI](https://fastapi.tiangolo.com/) - Alta performance, tipagem forte e documentação automática (Swagger/ReDoc).
- **ORM & Database**: 
  - [SQLModel](https://sqlmodel.tiangolo.com/) - Interação com o banco de dados e validação de dados baseada no Pydantic e SQLAlchemy.
  - [PostgreSQL](https://www.postgresql.org/) - Banco de dados relacional robusto (rodando via Docker).
  - [Alembic](https://alembic.sqlalchemy.org/) - Gerenciamento de migrações do banco de dados.
- **Gerenciamento de Pacotes**: [Uv](https://github.com/astral-sh/uv) - Resolução rápida de dependências (através de `pyproject.toml` e `uv.lock`).
- **Qualidade de Código & Testes**:
  - [Ruff](https://docs.astral.sh/ruff/) - Linter e formatador de código extremamente rápido.
  - [Pytest](https://docs.pytest.org/en/stable/) - Framework para a criação e execução de testes.

## 📂 Organização das Pastas

A arquitetura do projeto foca em modularidade (baseada no conceito de Feature Modules) para alta coesão e baixo acoplamento:

```text
backend/
├── alembic/              # Configurações e versões de migração do banco de dados
├── app/                  # Código-fonte principal da aplicação
│   ├── core/             # Configurações gerais (settings), conexões de banco e exceções base
│   ├── modules/          # Módulos funcionais separados por contexto de negócio (ex: suppliers)
│   │   └── suppliers/    # Domínio de fornecedores (Router, Service, Repository, Model, Schema)
│   ├── shared/           # Recursos compartilhados (Interfaces, Utils, Dependências e Seeders)
│   └── main.py           # Ponto de entrada (Entrypoint) da aplicação FastAPI
├── tests/                # Testes unitários e de integração
├── Makefile              # Atalhos para comandos comuns (dev-up, test, lint, etc.)
├── docker-compose.yaml   # Configuração do banco de dados local com Docker
├── pyproject.toml        # Configurações do projeto e dependências (PEP 621)
└── uv.lock               # Lockfile de dependências gerado pelo Uv
```

## 🛠️ Como Rodar o Projeto

Para executar o sistema localmente, siga os passos abaixo:

### 1. Pré-requisitos
- Ter o **Python 3.12+** instalado na máquina.
- Ter o **Docker** e o **Docker Compose** instalados (para rodar o banco de dados).
- Ter o gerenciador **Uv** instalado (`pip install uv`).

### 2. Configurando o Ambiente

Clone o repositório e crie o arquivo de configuração (se ainda não existir) baseado no contexto de banco de dados e outras chaves necessárias:

Certifique-se de que o arquivo `.env` está configurado corretamente na raiz do backend (contendo variáveis como `POSTGRES_USER`, `POSTGRES_PASSWORD`, e `POSTGRES_DB`).

### 3. Subindo o Banco de Dados

Suba o container do PostgreSQL em background:
```bash
docker-compose up -d
```

### 4. Instalando Dependências

Para instalar as dependências e criar o ambiente virtual, utilize o Uv:
```bash
uv sync
```
*Isso criará e ativará automaticamente as bibliotecas contidas no `pyproject.toml` para o ambiente via `.venv`.*

### 5. Executando as Migrações do Banco

Aplique a estrutura atualizada das tabelas no banco de dados via Alembic:
```bash
uv run alembic upgrade head
```
*(Opcional)* Você pode rodar o seed do banco caso necessite de dados iniciais, chamando o script correspondente que fica em `app/shared/seed.py`.

### 6. Subindo o Servidor

O projeto contém um `Makefile` com comandos úteis. Para rodar o servidor em modo de desenvolvimento (hot-reload):

```bash
make dev-up
```
A API estará acessível em `http://127.0.0.1:8000`. 
Acesse `http://127.0.0.1:8000/docs` para visualizar a documentação interativa (Swagger UI).

## 📜 Comandos Úteis do Makefile

Para ajudar no fluxo de desenvolvimento, os seguintes comandos estão disponíveis:

- `make dev-up`: Inicia a aplicação usando o servidor do FastAPI.
- `make check`: Verifica a formatação e roda o linter utilizando o Ruff.
- `make lint`: Corrige problemas identificados pelo linter e formata o código automaticamente.
- `make test`: Roda toda a suíte de testes com o pytest.
