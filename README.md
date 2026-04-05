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