# Plano de Modernização - Grimório Mágico para Web

## 📋 Visão Geral
Conversão da aplicação desktop Tkinter para uma aplicação web moderna com:
- **Backend**: Python Flask/FastAPI
- **Frontend**: React/Vue.js
- **Banco de Dados**: SQLite → PostgreSQL (opcional) 
- **API REST**: Contrato de dados em JSON

---

## 📊 Estrutura de Dados (Contrato JSON)

### 1. **Modelo de Feitiço**
```json
{
  "id": "uuid",
  "nome": "string (max 100)",
  "nivel": "number (0-9)",
  "escola": "string (max 100)",
  "tempo": "string (max 100)",
  "alcance": "string (max 100)",
  "componentes": "string (max 500)",
  "duracao": "string (max 100)",
  "descricao": "string (max 5000)",
  "criado_em": "ISO8601",
  "atualizado_em": "ISO8601"
}
```

### 2. **Resposta de API (Padrão)**
```json
{
  "sucesso": "boolean",
  "dados": "object ou array",
  "mensagem": "string",
  "codigo": "number",
  "timestamp": "ISO8601"
}
```

### 3. **Grimório (Coleção)**
```json
{
  "id": "uuid",
  "nome": "string",
  "descricao": "string",
  "total_feiticos": "number",
  "feiticos": ["array de IDs ou objetos completos"],
  "criado_em": "ISO8601",
  "atualizado_em": "ISO8601"
}
```

---

## 🏗️ Arquitetura da Aplicação Web

```
grimorio-web/
├── backend/
│   ├── app.py                 # Aplicação Flask/FastAPI
│   ├── models/
│   │   ├── feitico.py        # Modelo de Feitiço
│   │   └── grimorio.py       # Modelo de Grimório
│   ├── routes/
│   │   ├── feiticos.py       # Endpoints de Feitiços
│   │   └── grimorio.py       # Endpoints de Grimório
│   ├── database/
│   │   ├── connection.py     # Gerenciador de conexão
│   │   └── migrations.py     # Migrações
│   ├── services/
│   │   └── feitico_service.py # Lógica de negócio
│   ├── config.py             # Configurações
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FeiticoForm.jsx
│   │   │   ├── FeiticoList.jsx
│   │   │   └── FeiticoDetail.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Grimorio.jsx
│   │   │   └── Admin.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
└── docs/
    ├── API.md               # Documentação da API
    └── CONTRATO_DADOS.md   # Contrato de dados detalhado
```

---

## 🔌 Endpoints REST (API Specification)

### Feitiços
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/feiticos` | Listar todos |
| GET | `/api/v1/feiticos?escola=Magia%20Branca` | Filtrar por escola |
| GET | `/api/v1/feiticos?search=termo` | Buscar por nome |
| GET | `/api/v1/feiticos/{id}` | Obter um feitiço |
| POST | `/api/v1/feiticos` | Criar novo |
| PUT | `/api/v1/feiticos/{id}` | Atualizar |
| DELETE | `/api/v1/feiticos/{id}` | Deletar |

### Grimório
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/grimorio` | Informações do grimório |
| GET | `/api/v1/grimorio/stats` | Estatísticas |
| POST | `/api/v1/grimorio/backup` | Criar backup |
| GET | `/api/v1/grimorio/export` | Exportar dados |
| POST | `/api/v1/grimorio/import` | Importar dados |

---

## ✅ Fases de Implementação

### **Fase 1: Backend API (Semana 1-2)**
- [ ] Criar estrutura Flask/FastAPI
- [ ] Implementar modelos de dados
- [ ] Criar endpoints CRUD para feitiços
- [ ] Migrar dados do SQLite
- [ ] Autenticação básica (JWT)
- [ ] Documentação Swagger

### **Fase 2: Persistência de Dados (Semana 2)**
- [ ] Manter suporte a SQLite
- [ ] Adicionar suporte a PostgreSQL
- [ ] Sistema de backup automático
- [ ] Versionamento de dados

### **Fase 3: Frontend (Semana 3-4)**
- [ ] Setup Vite + React/Vue
- [ ] Componentes de visualização
- [ ] Formulários de edição
- [ ] Busca e filtros
- [ ] Design responsivo

### **Fase 4: Deploy (Semana 4)**
- [ ] Containerização Docker
- [ ] CI/CD Pipeline
- [ ] Deploy em nuvem (Heroku, Railway, etc)

---

## 🔄 Migração de Dados

### Conversão JSON
```json
{
  "Fireball": {
    "nível": "3",
    "escola": "Evocação",
    "tempo": "1 ação",
    "alcance": "150 pés",
    "componentes": "V, S, M",
    "duração": "Instantânea",
    "descrição": "Uma bola de fogo explode..."
  }
}
```

Será convertido para:
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "nome": "Fireball",
  "nivel": 3,
  "escola": "Evocação",
  "tempo": "1 ação",
  "alcance": "150 pés",
  "componentes": "V, S, M",
  "duracao": "Instantânea",
  "descricao": "Uma bola de fogo explode...",
  "criado_em": "2026-01-26T10:00:00Z",
  "atualizado_em": "2026-01-26T10:00:00Z"
}
```

---

## 🛠️ Tecnologias Recomendadas

### Backend
- **Framework**: FastAPI (moderno, rápido, validação automática)
- **ORM**: SQLAlchemy
- **Banco**: SQLite (dev) + PostgreSQL (prod)
- **Auth**: JWT com python-jose
- **API Docs**: Swagger/OpenAPI automático

### Frontend
- **Build**: Vite
- **Framework**: React 18 ou Vue 3
- **State Management**: Zustand ou Pinia
- **UI Framework**: Tailwind CSS
- **HTTP Client**: Axios

### Infraestrutura
- **Containerização**: Docker + Docker Compose
- **Web Server**: Nginx (reverse proxy)
- **Process Manager**: Gunicorn/Uvicorn
- **Banco Prod**: PostgreSQL 14+

---

## 📝 Próximos Passos

1. **Criar estrutura base do backend FastAPI**
2. **Definir models SQLAlchemy com validação Pydantic**
3. **Implementar endpoints CRUD com resposta JSON padronizada**
4. **Criar script de migração de dados (JSON → BD relacional)**
5. **Setup frontend com Vite + React**
6. **Implementar componentes principais**
7. **Integração backend-frontend**
8. **Deploy**

---

## 📚 Referências
- OpenAPI/Swagger: https://swagger.io/
- FastAPI Docs: https://fastapi.tiangolo.com/
- React Docs: https://react.dev/
- SQLAlchemy ORM: https://docs.sqlalchemy.org/
