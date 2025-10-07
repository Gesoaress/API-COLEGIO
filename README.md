# 🏫 API Colégio — Flask + SQLite + Swagger + Docker

Este projeto implementa uma API completa para gerenciamento de **Professores**, **Turmas** e **Alunos**, utilizando Flask e SQLAlchemy, com documentação interativa via Swagger e suporte a execução via Docker.

---

## 🚀 Funcionalidades Principais

✅ CRUD completo para Professores, Turmas e Alunos  
✅ Persistência com SQLite (ORM SQLAlchemy)  
✅ Estrutura MVC (Model - Controller - sem View)  
✅ Documentação Swagger via Flasgger  
✅ Containerização com Docker  
✅ Código versionado no GitHub  

---

## ⚙️ Estrutura do Projeto

```
api-colegio/
│
├── app/
│   ├── __init__.py          # Criação e configuração do app Flask
│   ├── extensions.py        # Instância do SQLAlchemy
│   ├── models/              # Modelos do banco (Professor, Turma, Aluno)
│   ├── controllers/         # Rotas e lógica de CRUD
│   └── docs/                # Arquivos YAML do Swagger
│
├── instance/                # Banco de dados SQLite (gerado automaticamente)
├── requirements.txt         # Dependências do projeto
├── Dockerfile               # Instruções para build da imagem Docker
├── docker-compose.yml       # Configuração do serviço Docker
├── .dockerignore            # Arquivos ignorados pelo Docker
├── .gitignore               # Arquivos ignorados pelo Git
└── run.py                   # Arquivo principal para executar o app
```

---

## 💻 Execução Local (sem Docker)

### 1️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Rodar o servidor

```bash
python run.py
```

Acesse: 👉 http://127.0.0.1:5000/apidocs/

---

## 🐳 Execução com Docker

### 📦 Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e em execução  
- [Docker Compose](https://docs.docker.com/compose/install/) (já vem junto com o Docker Desktop)

---

### 🚀 Passo a passo

1️⃣ **Clone o repositório**
```bash
git clone https://github.com/<seu-usuario>/<nome-do-repositorio>.git
cd <nome-do-repositorio>
```

2️⃣ **Construa e suba o container**
```bash
docker-compose up --build
```

3️⃣ **Acesse a API**
Depois que o build terminar, o terminal exibirá algo como:

```
* Running on http://0.0.0.0:5000
```

Acesse no navegador:
👉 **http://127.0.0.1:5000/apidocs/**  

Lá estará a documentação Swagger com todos os endpoints disponíveis.

---

### ⚙️ Comandos úteis

| Ação | Comando |
|------|----------|
| Rodar em segundo plano | `docker-compose up -d` |
| Parar o container | `docker-compose down` |
| Ver logs em tempo real | `docker-compose logs -f` |
| Ver containers ativos | `docker ps` |
| Remover imagens e containers antigos | `docker system prune -f` |

---

### 💾 Banco de Dados

O banco **SQLite** é criado automaticamente dentro da pasta `instance/` no container.  
Graças ao volume configurado em `docker-compose.yml`, os dados são persistidos entre execuções.

---

### 🧩 Estrutura Docker

| Arquivo | Função |
|----------|--------|
| `Dockerfile` | Define como a imagem é construída (instala dependências e roda o app). |
| `.dockerignore` | Evita copiar arquivos desnecessários (venv, cache, etc.). |
| `docker-compose.yml` | Define os serviços, volumes e portas. |

---

## 👥 Autor
Geovane Soares da Silva
Richard Ferreira 

Projeto desenvolvido para a disciplina de **Desenvolvimento de APIs e Microsserviços (DAM)**.

📘 **Licença:** Uso acadêmico e educacional.
