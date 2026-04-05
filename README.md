# FlowOps

Plataforma de automação e orquestração de processos, desenvolvida para simular um projeto real de mercado com foco em APIs, processamento assíncrono, filas, integrações e observabilidade.

## Objetivo

O FlowOps tem como objetivo centralizar execuções automatizadas de processos, permitindo que eventos recebidos por API sejam processados, registrados e monitorados de forma organizada.

Nesta fase inicial, o projeto foi preparado com a fundação necessária para evoluir para:

- workflows automatizados
- processamento em background
- integrações externas
- monitoramento de execuções
- histórico de tarefas

## Stack inicial

- Python
- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Alembic
- Docker
- Docker Compose

## Estrutura do projeto

```text
flowops/
├── app/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   │   └── config.py
│   ├── integrations/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── workers/
│   └── main.py
├── tests/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

## Funcionalidades atuais

- Inicialização da API com FastAPI
- Configuração centralizada com variáveis de ambiente
- Endpoint raiz para validação da aplicação
- Endpoint `/health` para health check
- Documentação automática com Swagger em `/docs`
- Ambiente containerizado com Docker Compose
- Serviços preparados:
  - app
  - PostgreSQL
  - Redis

## Endpoints disponíveis

### `GET /`
Retorna uma mensagem simples informando que a API está em execução.

### `GET /health`
Retorna o status básico da aplicação.

### `GET /docs`
Abre a documentação interativa gerada automaticamente pelo FastAPI.

## Como executar localmente

### 1. Criar e ativar ambiente virtual

No Windows com Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Criar o arquivo `.env`

Use o `.env.example` como base.

### 4. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000
```

## Como executar com Docker

```bash
docker compose up --build
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8001
```

## Variáveis de ambiente

Exemplo de configuração:

```env
APP_NAME=FlowOps
APP_ENV=development
APP_HOST=0.0.0.0
APP_PORT=8000
DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/flowops
REDIS_URL=redis://redis:6379/0
```

## Status do projeto

Sprint 0 concluída.

### Entregas finalizadas nesta sprint

- Estrutura inicial do projeto
- Configuração centralizada
- API base com FastAPI
- Health check
- Dockerfile
- Docker Compose com app, PostgreSQL e Redis
- Ambiente validado localmente e via containers

## Próximos passos

Sprint 1:

- modelagem inicial de domínio
- integração com banco
- criação das entidades principais
- schemas com Pydantic
- primeiro fluxo de persistência

## Observações

Durante a configuração do ambiente, houve necessidade de ajuste de portas no Docker Compose para evitar conflito com outros projetos locais já existentes. A aplicação foi exposta na porta `8001` no host, mantendo a porta `8000` internamente no container.
