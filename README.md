# TerrariumHub 🐢

Sistema de monitoramento de terrário desenvolvido com Python, ESP32 e Docker, com o objetivo de acompanhar condições ambientais e centralizar as leituras em uma API.

## Tecnologias

- **MicroPython / ESP32:** firmware, conexão Wi-Fi e coleta de dados
- **Python / FastAPI:** API REST para receber e consultar medições
- **SQLAlchemy / MariaDB:** persistência dos dados
- **Docker / Docker Compose:** execução dos serviços em containers
- **Telegram:** módulo de integração para notificações

## Arquitetura

- `esp32/` — firmware e módulos do ESP32
- `app/` — API, modelos, schemas, rotas e serviços
- `Dockerfile` — imagem da API
- `docker-compose.yml` — serviços da API e do MariaDB

## Executar com Docker

### Pré-requisitos

- Docker Desktop com Docker Compose
- Git

### Configuração

1. Clone o repositório.
2. Copie `.env.example` para `.env`.
3. Configure as senhas e a variável `DATABASE_URL`, mantendo as credenciais consistentes.
4. Inicie os serviços:

```bash
docker compose up --build -d
```

Consulte os logs com:

```bash
docker compose logs -f
```

Quando a API estiver em execução, acesse:

- **Documentação interativa:** http://localhost:8000/docs
- **Status da API:** http://localhost:8000/medicoes/status

Para encerrar os containers:

```bash
docker compose down
```

## Objetivos do projeto

- Desenvolver uma solução de IoT com ESP32 e Python
- Integrar dispositivos físicos a uma API REST
- Praticar persistência de dados e comunicação entre serviços
- Aplicar Docker e organização de código em um projeto prático

> Projeto de portfólio em desenvolvimento. A configuração e os fluxos de integração devem ser validados no ambiente de execução antes do uso contínuo.
