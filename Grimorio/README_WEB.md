# 🚀 Grimório Mágico v2.0 - Aplicação Web

Transformação completa do **Grimório Mágico** de uma aplicação desktop (Tkinter) para uma **aplicação web moderna** com arquitetura cliente-servidor.

## 📋 Visão Geral

```
┌─────────────────────────────────────────┐
│        Frontend (React + Vite)          │
│  http://localhost:5173                  │
└────────────────┬────────────────────────┘
                 │ HTTP/JSON
                 ↓
┌─────────────────────────────────────────┐
│    Backend (FastAPI)                    │
│  http://localhost:8000/api/v1           │
└────────────────┬────────────────────────┘
                 │ SQL
                 ↓
┌─────────────────────────────────────────┐
│    Banco de Dados                       │
│    SQLite / PostgreSQL                  │
└─────────────────────────────────────────┘
```

---

## ✨ O que mudou?

### Desktop (Antigo) → Web (Novo)

| Aspecto | Desktop (Tkinter) | Web (React + FastAPI) |
|---------|-------------------|----------------------|
| Interface | Tkinter GUI | HTML5 + CSS3 (Tailwind) |
| Backend | Lógica embarcada | API REST |
| Banco de Dados | SQLite local | SQLite/PostgreSQL |
| Dados | JSON + SQLite | JSON estruturado |
| Acesso | Local | Via Browser/HTTP |
| Escalabilidade | Limitada | Ilimitada |
| Deployment | .exe | Web (Docker, Cloud) |

---

## 📁 Estrutura do Projeto

```
Grimorio/
├── backend/                    # API FastAPI
│   ├── main.py                # Aplicação principal
│   ├── config.py              # Configurações
│   ├── schemas.py             # Modelos Pydantic
│   ├── models.py              # Modelos SQLAlchemy
│   ├── database.py            # Gerenciador BD
│   ├── services.py            # Lógica de negócio
│   ├── migrate.py             # Script de migração
│   ├── requirements.txt        # Dependências Python
│   ├── API.md                 # Documentação API
│   ├── README.md              # Backend README
│   └── .env.example           # Variáveis de ambiente
│
├── frontend/                   # Aplicação React
│   ├── src/
│   │   ├── components/        # Componentes React
│   │   ├── services/          # Cliente HTTP
│   │   ├── App.jsx            # Componente principal
│   │   ├── main.jsx           # Entrada
│   │   └── index.css          # Estilos globais
│   ├── public/                # Assets estáticos
│   ├── index.html             # Template HTML
│   ├── package.json           # Dependências npm
│   ├── vite.config.js         # Configuração Vite
│   ├── tailwind.config.js     # Configuração Tailwind
│   ├── README.md              # Frontend README
│   └── .env.example           # Variáveis de ambiente
│
├── docs/                      # Documentação
│   ├── CONTRATO_DADOS.md     # Especificação JSON
│   ├── ARQUITETURA.md        # Diagrama de arquitetura
│   └── DEPLOYMENT.md         # Guia de deploy
│
├── docker-compose.yml         # Composição Docker
├── .gitignore                 # Git ignore
├── PLANO_MODERNIZACAO_WEB.md # Plano completo
└── README.md                  # Este arquivo
```

---

## 🚀 Quick Start

### Pré-requisitos

- Node.js 18+
- Python 3.9+
- Docker (opcional)

### 1️⃣ Backend

```bash
# Instalar dependências
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Criar arquivo .env
cp .env.example .env

# Executar
python main.py
# API rodando em: http://localhost:8000
# Docs em: http://localhost:8000/docs
```

### 2️⃣ Frontend

```bash
# Instalar dependências
cd frontend
npm install

# Executar
npm run dev
# Aplicação rodando em: http://localhost:5173
```

### 3️⃣ Pronto!

Acesse: **http://localhost:5173**

---

## 📊 Especificação de Dados (Contrato JSON)

### Feitiço
```json
{
  "id": 1,
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

### Resposta Paginada
```json
{
  "itens": [],
  "total": 150,
  "pagina": 1,
  "por_pagina": 20,
  "total_paginas": 8,
  "sucesso": true,
  "mensagem": "Ok",
  "timestamp": "2026-01-26T10:00:00Z"
}
```

---

## 🔌 API REST Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/feiticos` | Listar feitiços |
| GET | `/api/v1/feiticos/{id}` | Obter um |
| POST | `/api/v1/feiticos` | Criar novo |
| PUT | `/api/v1/feiticos/{id}` | Atualizar |
| DELETE | `/api/v1/feiticos/{id}` | Deletar |
| GET | `/api/v1/feiticos/buscar?termo=...` | Buscar |
| GET | `/api/v1/feiticos/escola?escola=...` | Filtrar escola |
| GET | `/api/v1/feiticos/nivel?nivel=...` | Filtrar nível |
| GET | `/api/v1/grimorio` | Info grimório |
| GET | `/api/v1/grimorio/stats` | Estatísticas |

---

## 🛠️ Stack Tecnológico

### Backend
- **Framework**: FastAPI
- **Banco de Dados**: SQLAlchemy + SQLite/PostgreSQL
- **Validação**: Pydantic
- **Servidor**: Uvicorn
- **Documentação**: Swagger/OpenAPI

### Frontend
- **Framework**: React 18
- **Build**: Vite
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios
- **Responsividade**: Mobile-first

### DevOps
- **Containerização**: Docker
- **Orquestração**: Docker Compose
- **CI/CD**: GitHub Actions (opcional)

---

## 🔄 Migração de Dados

Se você tem dados da versão anterior:

```bash
cd backend
python migrate.py
```

Este script irá importar dados de:
- `grimorio.json` (formato antigo)
- `grimorio.db` (SQLite antigo)

---

## 📝 Documentação

- [Backend API Docs](backend/API.md)
- [Backend README](backend/README.md)
- [Frontend README](frontend/README.md)
- [Plano de Modernização](PLANO_MODERNIZACAO_WEB.md)

---

## 🐳 Deploy com Docker

### Docker Compose

```bash
docker-compose up -d
```

Acesse:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Docs API: http://localhost:8000/docs

---

## 🚢 Deploy em Produção

### Heroku
```bash
# Backend
cd backend
heroku create grimorio-api
git push heroku main

# Frontend
cd frontend
npm run build
heroku create grimorio-web
git push heroku main
```

### Railway / Render / Vercel
Veja guia completo em `docs/DEPLOYMENT.md`

---

## 🔐 Segurança

### Antes de ir para Produção

1. **Altere `SECRET_KEY`** em `.env`:
   ```env
   SECRET_KEY=sua-chave-muito-segura-aqui
   ```

2. **Configure CORS**:
   ```env
   CORS_ORIGINS=https://seudominio.com
   ```

3. **Use PostgreSQL** em produção:
   ```env
   DATABASE_URL=postgresql://user:pass@host/db
   ```

4. **Habilite HTTPS** com certificado SSL

5. **Configure backup automático** do banco de dados

---

## 📊 Funcionalidades

✅ Criar/Editar/Deletar feitiços
✅ Buscar feitiços por nome
✅ Filtrar por escola de magia
✅ Filtrar por nível (0-9)
✅ Visualizar estatísticas
✅ Paginação inteligente
✅ Interface responsiva
✅ Documentação da API
✅ Migração de dados automática
✅ Sistema de backup

---

## 🧪 Testes

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm run test
```

---

## 🐛 Troubleshooting

### CORS Error
```
Access to XMLHttpRequest... blocked by CORS policy
```
→ Verifique `CORS_ORIGINS` no `.env` do backend

### Connection Refused
```
connect ECONNREFUSED 127.0.0.1:8000
```
→ Certifique-se que o backend está rodando em `http://localhost:8000`

### Port Already in Use
```bash
# Backend
lsof -ti:8000 | xargs kill -9
python main.py

# Frontend
npm run dev -- --port 5174
```

---

## 📈 Próximos Passos

- [ ] Autenticação com JWT
- [ ] Importar/Exportar dados
- [ ] Backup automático
- [ ] Sistema de favoritos
- [ ] Notas personalizadas
- [ ] Sincronização em nuvem
- [ ] Aplicativo mobile (React Native)
- [ ] Testes automatizados
- [ ] CI/CD com GitHub Actions

---

## 🤝 Contribuindo

```bash
# Clone o repositório
git clone <repo>
cd Grimorio

# Crie uma branch
git checkout -b feature/nova-feature

# Commit suas mudanças
git commit -am 'Add nova feature'

# Push para a branch
git push origin feature/nova-feature

# Abra um Pull Request
```

---

## 📄 Licença

MIT License - veja LICENSE.md para detalhes

---

## 👥 Autor

Desenvolvido com ✨ como projeto de modernização

---

## 📞 Suporte

- 📚 Documentação: Veja pasta `docs/`
- 🐛 Issues: GitHub Issues
- 💬 Discussões: GitHub Discussions

---

## 🎉 Conclusão

A transformação de **Grimório Mágico** para uma aplicação web moderna oferece:

- ✅ Acesso via navegador
- ✅ Melhor escalabilidade
- ✅ Arquitetura limpa e profissional
- ✅ Facilidade de manutenção
- ✅ Possibilidade de deploy em nuvem
- ✅ Contrato de dados estruturado em JSON

**Bem-vindo ao futuro do Grimório!** 🧙‍♂️✨
