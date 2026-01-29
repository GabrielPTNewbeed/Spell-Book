# Grimório Mágico - Backend API

## 📚 Documentação da API

### Visão Geral
API REST construída com FastAPI para gerenciar uma coleção de feitiços mágicos. A API segue padrões REST e retorna dados em formato JSON.

### Base URL
```
http://localhost:8000/api/v1
```

### Documentação Interativa
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🔌 Endpoints

### 1. Health Check

#### GET `/health`
Verifica o status da API.

**Resposta (200):**
```json
{
  "status": "ok",
  "aplicacao": "Grimório Mágico API",
  "versao": "2.0.0",
  "timestamp": "2026-01-26T10:00:00"
}
```

---

### 2. Feitiços

#### GET `/feiticos`
Lista todos os feitiços com paginação.

**Query Parameters:**
- `skip` (int, default=0): Número de registros a pular
- `limit` (int, default=20, max=100): Número de registros a retornar
- `ordem` (string, default="nome"): Campo de ordenação (nome, nivel, recente)

**Resposta (200):**
```json
{
  "itens": [
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
      "criado_em": "2026-01-26T10:00:00",
      "atualizado_em": "2026-01-26T10:00:00"
    }
  ],
  "total": 150,
  "pagina": 1,
  "por_pagina": 20,
  "total_paginas": 8,
  "sucesso": true,
  "mensagem": "Feitiços recuperados com sucesso",
  "timestamp": "2026-01-26T10:00:00"
}
```

---

#### GET `/feiticos/{id}`
Obter detalhes de um feitiço específico.

**Path Parameters:**
- `id` (int): ID do feitiço

**Resposta (200):**
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
  "criado_em": "2026-01-26T10:00:00",
  "atualizado_em": "2026-01-26T10:00:00"
}
```

**Respostas de Erro:**
- 404: Feitiço não encontrado

---

#### POST `/feiticos`
Criar um novo feitiço.

**Request Body:**
```json
{
  "nome": "Magic Missile",
  "nivel": 1,
  "escola": "Evocação",
  "tempo": "1 ação",
  "alcance": "120 pés",
  "componentes": "V, S",
  "duracao": "Instantânea",
  "descricao": "Você lança um míssil de magia pura..."
}
```

**Resposta (201):**
```json
{
  "id": 2,
  "nome": "Magic Missile",
  "nivel": 1,
  "escola": "Evocação",
  "tempo": "1 ação",
  "alcance": "120 pés",
  "componentes": "V, S",
  "duracao": "Instantânea",
  "descricao": "Você lança um míssil de magia pura...",
  "criado_em": "2026-01-26T10:00:00",
  "atualizado_em": "2026-01-26T10:00:00"
}
```

**Respostas de Erro:**
- 400: Validação de dados falhou
- 409: Feitiço já existe

---

#### PUT `/feiticos/{id}`
Atualizar um feitiço existente.

**Path Parameters:**
- `id` (int): ID do feitiço

**Request Body (todos os campos são opcionais):**
```json
{
  "nivel": 2,
  "descricao": "Descrição atualizada..."
}
```

**Resposta (200):** Feitiço atualizado

**Respostas de Erro:**
- 404: Feitiço não encontrado

---

#### DELETE `/feiticos/{id}`
Deletar um feitiço.

**Path Parameters:**
- `id` (int): ID do feitiço

**Resposta (204):** Sem conteúdo (sucesso)

**Respostas de Erro:**
- 404: Feitiço não encontrado

---

#### GET `/feiticos/buscar`
Buscar feitiços por nome.

**Query Parameters:**
- `termo` (string, required): Termo de busca
- `skip` (int, default=0): Número de registros a pular
- `limit` (int, default=20, max=100): Número de registros a retornar

**Resposta (200):** Lista paginada de feitiços

---

#### GET `/feiticos/escola`
Filtrar feitiços por escola de magia.

**Query Parameters:**
- `escola` (string, required): Nome da escola
- `skip` (int, default=0): Número de registros a pular
- `limit` (int, default=20, max=100): Número de registros a retornar

**Resposta (200):** Lista paginada de feitiços

---

#### GET `/feiticos/nivel`
Filtrar feitiços por nível.

**Query Parameters:**
- `nivel` (int, required): Nível (0-9)
- `skip` (int, default=0): Número de registros a pular
- `limit` (int, default=20, max=100): Número de registros a retornar

**Resposta (200):** Lista paginada de feitiços

---

### 3. Grimório

#### GET `/grimorio`
Obter informações do grimório principal.

**Resposta (200):**
```json
{
  "id": 1,
  "nome": "Grimório Principal",
  "descricao": "Grimório principal da coleção de mágica",
  "criado_em": "2026-01-26T10:00:00",
  "atualizado_em": "2026-01-26T10:00:00",
  "total_feiticos": 150
}
```

---

#### GET `/grimorio/stats`
Obter estatísticas do grimório.

**Resposta (200):**
```json
{
  "sucesso": true,
  "dados": {
    "total_feiticos": 150,
    "feiticos_por_nivel": {
      "0": 10,
      "1": 20,
      "2": 25,
      "3": 35,
      "4": 30,
      "5": 10
    },
    "feiticos_por_escola": {
      "Evocação": 45,
      "Abjuração": 30,
      "Ilusão": 25,
      "Encantamento": 20,
      "Divinação": 15,
      "Conjuração": 10,
      "Transmutação": 5
    }
  },
  "mensagem": "Estatísticas recuperadas com sucesso",
  "codigo": 200,
  "timestamp": "2026-01-26T10:00:00"
}
```

---

## 📋 Estrutura de Dados

### Feitiço
```json
{
  "id": 1,
  "nome": "string (1-100 caracteres)",
  "nivel": "integer (0-9)",
  "escola": "string (até 100 caracteres)",
  "tempo": "string (até 100 caracteres)",
  "alcance": "string (até 100 caracteres)",
  "componentes": "string (até 500 caracteres)",
  "duracao": "string (até 100 caracteres)",
  "descricao": "string (até 5000 caracteres)",
  "criado_em": "ISO8601 datetime",
  "atualizado_em": "ISO8601 datetime"
}
```

### Resposta Paginada
```json
{
  "itens": "array de objetos",
  "total": "integer - total de itens",
  "pagina": "integer - página atual",
  "por_pagina": "integer - itens por página",
  "total_paginas": "integer - total de páginas",
  "sucesso": "boolean",
  "mensagem": "string",
  "timestamp": "ISO8601 datetime"
}
```

---

## 🔄 Códigos HTTP

| Código | Significado |
|--------|------------|
| 200 | OK - Requisição bem-sucedida |
| 201 | Created - Recurso criado com sucesso |
| 204 | No Content - Requisição bem-sucedida (sem conteúdo) |
| 400 | Bad Request - Dados inválidos |
| 404 | Not Found - Recurso não encontrado |
| 409 | Conflict - Recurso já existe |
| 500 | Internal Server Error - Erro do servidor |

---

## 🚀 Exemplos de Uso

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
    "descricao": "Uma bola de fogo explode..."
  }'
```

### Listar feitiços
```bash
curl http://localhost:8000/api/v1/feiticos?skip=0&limit=10&ordem=nome
```

### Buscar por termo
```bash
curl http://localhost:8000/api/v1/feiticos/buscar?termo=fire
```

### Filtrar por escola
```bash
curl http://localhost:8000/api/v1/feiticos/escola?escola=Evocação
```

### Obter estatísticas
```bash
curl http://localhost:8000/api/v1/grimorio/stats
```

---

## 📝 Notas

- Todas as datas estão no formato ISO8601 (UTC)
- Nomes de feitiços são únicos
- O nível varia de 0 (truque/cantrip) a 9 (feitiço de nível 9)
- Paginação começa em 0 (skip=0 é a primeira página)
