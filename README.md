# Todo API

Uma API REST para gerenciamento de tarefas desenvolvida com FastAPI e SQLAlchemy.

## 📋 Funcionalidades

- ✅ **Autenticação de usuários** - Sistema de login seguro com hash de senha
- 👤 **Gerenciamento de usuários** - Criação e gerenciamento de contas
- 📝 **CRUD de tarefas** - Criar, listar, atualizar e deletar tarefas
- 🏷️ **Sistema de status** - Controle de status das tarefas (Backlog, Todo, In Progress, Finished, Cancelled)
- 🔐 **Middleware de autenticação** - Proteção das rotas com autenticação
- 📍 **Endereços** - Integração com CEP para endereços de usuários

## 🛠️ Tecnologias

- **FastAPI** - Framework web moderno e rápido para APIs
- **SQLAlchemy** - ORM para Python
- **SQLite** - Banco de dados (db.sqlite3)
- **Bcrypt** - Criptografia de senhas
- **Loguru** - Sistema de logging
- **Pydantic** - Validação de dados com schemas

## 📁 Estrutura do Projeto

```
src/
├── config/          # Configurações do banco e dependências
├── enums/           # Enumerações (StatusTask)
├── middlewares/     # Middleware de autenticação
├── models/          # Modelos SQLAlchemy (User, Task)
├── repositories/    # Camada de repositório para acesso aos dados
├── routes/          # Rotas da API (auth, users, tasks)
├── schemas/         # Schemas Pydantic para validação
└── main.py          # Arquivo principal da aplicação
```

## 🚀 Como executar

### Pré-requisitos

- Python 3.13+
- UV (gerenciador de pacotes Python)

### Instalação

1. **Instale o UV** (se ainda não tiver):
```bash
# No macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# No Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Clone o repositório:
```bash
git clone https://github.com/giovaninogueira/todo-python.git
cd todo-python
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

4. Instale as dependências com UV:
```bash
uv sync
```

5. Execute a aplicação:
```bash
uv run fastapi dev ./src/main.py
```

A API estará disponível em: `http://localhost:8000`

## 📖 Documentação da API

Após executar a aplicação, acesse:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔗 Endpoints Principais

### Autenticação
- `POST /auth/login` - Realizar login
- `POST /auth/register` - Registrar novo usuário

### Usuários
- `GET /users/` - Listar usuários
- `POST /users/` - Criar usuário
- `GET /users/{id}` - Obter usuário por ID
- `PUT /users/{id}` - Atualizar usuário
- `DELETE /users/{id}` - Deletar usuário

### Tarefas
- `GET /tasks/` - Listar tarefas do usuário autenticado
- `POST /tasks/` - Criar nova tarefa
- `GET /tasks/{id}` - Obter tarefa por ID
- `PUT /tasks/{id}` - Atualizar tarefa
- `DELETE /tasks/{id}` - Deletar tarefa
- `PATCH /tasks/{id}/status` - Atualizar status da tarefa

## 📊 Status das Tarefas

As tarefas podem ter os seguintes status:

- `BACKLOG` - Tarefa em backlog
- `TODO` - Tarefa a fazer
- `IN_PROGRESS` - Tarefa em progresso
- `FINISHED` - Tarefa finalizada
- `CANCELLED` - Tarefa cancelada

## 🗄️ Banco de Dados

O projeto utiliza SQLite como banco de dados padrão. O arquivo `db.sqlite3` é criado automaticamente na primeira execução.

### Modelos

- **User**: Usuários do sistema (nome, email, senha, endereço, CEP)
- **Task**: Tarefas dos usuários (título, descrição, status, data de criação/atualização)

## 🛡️ Segurança

- Senhas são criptografadas usando bcrypt
- Autenticação obrigatória para operações com tarefas
- Middleware de autenticação protege rotas sensíveis

## 📝 Scripts Disponíveis

### Usando UV (recomendado):
```bash
uv run fastapi dev ./src/main.py  # Executa a aplicação em modo desenvolvimento
uv sync                           # Instala/atualiza dependências
uv add <pacote>                   # Adiciona nova dependência
```

### Usando Makefile:
```bash
make run     # Executa a aplicação em modo desenvolvimento
make freeze  # Atualiza o requirements.txt com as dependências atuais
```

> **Nota**: O projeto agora usa UV como gerenciador de pacotes. O UV oferece instalação mais rápida de dependências e melhor gerenciamento de ambiente virtual.

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Giovani Cassiano**

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!