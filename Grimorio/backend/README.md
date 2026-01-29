# Grimório Mágico - Backend API

Uma API REST moderna construída com **FastAPI** para gerenciar uma coleção de feitiços mágicos.

## ✨ Features

- ✅ API REST completa com CRUD
- ✅ Documentação automática (Swagger + ReDoc)
- ✅ Validação de dados com Pydantic
- ✅ Paginação inteligente
- ✅ Busca e filtros avançados
- ✅ Suporte a SQLite e PostgreSQL
- ✅ Logging centralizado
- ✅ CORS configurável
- ✅ Migração de dados automática

## 🚀 Quick Start

### 1. Instalação

```bash
# Clonar repositório (se necessário)
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configuração

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar .env conforme necessário
# DEBUG=True
# DATABASE_URL=sqlite:///./grimorio.db
```

### 3. Executar

```bash
# Desenvolvimento (com hot reload)
python main.py

# Ou usando uvicorn diretamente
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: **http://localhost:8000**

### 4. Documentação

Acesse:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📁 Estrutura do Projeto

```
backend/
├── main.py                 # Aplicação FastAPI principal
├── config.py              # Configurações
├── schemas.py             # Modelos Pydantic (validação)
├── models.py              # Modelos SQLAlchemy (banco de dados)
├── database.py            # Gerenciador de banco de dados
├── services.py            # Lógica de negócio
├── migrate.py             # Script de migração de dados
├── requirements.txt       # Dependências Python
├── .env.example           # Exemplo de variáveis de ambiente
├── API.md                 # Documentação da API
└── README.md              # Este arquivo
```

---

## 🔌 Endpoints Principais

### Feitiços
- `GET /api/v1/feiticos` - Listar todos
- `GET /api/v1/feiticos/{id}` - Obter um
- `POST /api/v1/feiticos` - Criar novo
- `PUT /api/v1/feiticos/{id}` - Atualizar
- `DELETE /api/v1/feiticos/{id}` - Deletar
- `GET /api/v1/feiticos/buscar` - Buscar por nome
- `GET /api/v1/feiticos/escola` - Filtrar por escola
- `GET /api/v1/feiticos/nivel` - Filtrar por nível

### Grimório
- `GET /api/v1/grimorio` - Info principal
- `GET /api/v1/grimorio/stats` - Estatísticas

---

## 📊 Exemplo de Uso

### Criar um feitiço

```bash
curl -X POST http://localhost:8000/api/v1/feiticos \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Fireball",
    "nivel": 3,
    "escola": "Evocação",
    "tempo": "1 ação",
    "alcance": "150 pés",
    "componentes": "V, S, M",
    "duracao": "Instantânea",
    "descricao": "Uma bola de fogo explode em um ponto à sua escolha..."
  }'
```

### Listar feitiços

```bash
curl http://localhost:8000/api/v1/feiticos?skip=0&limit=20&ordem=nome
```

### Buscar feitiço

```bash
curl http://localhost:8000/api/v1/feiticos/buscar?termo=fire
```

---

## 🔄 Migração de Dados

Se você tem dados da versão anterior (Tkinter):

```bash
# Python
python migrate.py
```

Este script irá:
1. Ler dados do `grimorio.json` (se existir)
2. Ler dados do `grimorio.db` antigo (se existir)
3. Importar para o novo banco de dados

---

## 🗄️ Banco de Dados

### SQLite (Desenvolvimento)
```
DATABASE_URL=sqlite:///./grimorio.db
```

### PostgreSQL (Produção)
```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/grimorio
```

---

## 🔐 Segurança

### Variáveis de Ambiente Importantes

```env
# MUDE ISSO EM PRODUÇÃO!
SECRET_KEY=sua-chave-muito-secreta-e-aleatoria-aqui

# CORS - apenas domínios confiáveis
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# Debug
DEBUG=False  # Em produção!
```

---

## 📦 Dependências Principais

- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI
- **Python-jose** - JWT tokens
- **Psycopg2** - Driver PostgreSQL (opcional)

---

## 🧪 Testes

```bash
# Instalar pytest
pip install pytest pytest-asyncio

# Executar testes
pytest

# Com cobertura
pytest --cov=. --cov-report=html
```

---

## 📝 Logging

Logs são salvos em `logs/api.log` e exibidos no console.

```python
import logging
logger = logging.getLogger(__name__)
logger.info("Mensagem de info")
logger.error("Mensagem de erro")
```

---

## 🚢 Deploy

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t grimorio-api .
docker run -p 8000:8000 grimorio-api
```

### Heroku / Railway / Vercel

Veja documentação de cada plataforma.

---

## 🐛 Troubleshooting

### Erro: "Database is locked"
- Feche outras conexões ao banco SQLite
- Use PostgreSQL em produção

### Erro: "CORS error"
- Adicione sua URL frontend em `CORS_ORIGINS` no `.env`

### Erro de import
- Certifique-se que está no diretório `backend`
- Verifique que o `venv` está ativado

---

## 📚 Referências

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [OpenAPI/Swagger](https://swagger.io/)

---

## 📄 Licença

MIT

---

## 👤 Autor

Desenvolvido como parte do projeto **Grimório Mágico 2.0**

---

## 🤝 Contribuições

Pull requests são bem-vindos!

```bash
git checkout -b feature/nova-feature
git commit -am 'Add nova feature'
git push origin feature/nova-feature
```
