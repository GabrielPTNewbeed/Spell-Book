# 📋 Contrato de Dados - Grimório Mágico v2.0

## Visão Geral

Este documento especifica o contrato de dados em JSON para a API REST do Grimório Mágico v2.0.

Todos os dados são transmitidos em **JSON** com encoding **UTF-8** e timestamps em **ISO 8601** (UTC).

---

## 🔍 Tabela de Conteúdos

1. [Modelos de Dados](#modelos-de-dados)
2. [Respostas Padrão](#respostas-padrão)
3. [Validações](#validações)
4. [Exemplos](#exemplos)

---

## Modelos de Dados

### 1. Feitiço (Spell)

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

#### Campos Detalhados

| Campo | Tipo | Obrigatório | Validação | Descrição |
|-------|------|-------------|-----------|-----------|
| `id` | integer | ✅ | id > 0 | ID único (gerado pelo servidor) |
| `nome` | string | ✅ | 1-100 chars, único | Nome do feitiço |
| `nivel` | integer | ❌ | 0-9 | Nível do feitiço (0 = cantrip/truque) |
| `escola` | string | ❌ | max 100 chars | Escola de magia (ver escolas válidas) |
| `tempo` | string | ❌ | max 100 chars | Tempo de conjuração (ex: "1 ação") |
| `alcance` | string | ❌ | max 100 chars | Alcance do feitiço (ex: "150 pés") |
| `componentes` | string | ❌ | max 500 chars | Componentes necessários (V/S/M) |
| `duracao` | string | ❌ | max 100 chars | Duração do efeito (ex: "Instantânea") |
| `descricao` | string | ❌ | max 5000 chars | Descrição completa do feitiço |
| `criado_em` | datetime | ✅ | ISO 8601 UTC | Data de criação (auto) |
| `atualizado_em` | datetime | ✅ | ISO 8601 UTC | Data última atualização (auto) |

#### Escolas Válidas

- **Abjuração** - Proteção, prevenção
- **Conjuração** - Invocar criaturas/objetos
- **Divinação** - Obter informações
- **Encantamento** - Influenciar comportamento
- **Evocação** - Dano, energia
- **Ilusão** - Enganar sentidos
- **Necromancia** - Morte, não-mortos
- **Transmutação** - Transformação, mudança

---

### 2. Grimório

```json
{
  "id": 1,
  "nome": "Grimório Principal",
  "descricao": "Grimório principal da coleção de mágica",
  "criado_em": "2026-01-26T10:00:00Z",
  "atualizado_em": "2026-01-26T10:00:00Z",
  "total_feiticos": 150
}
```

#### Campos Detalhados

| Campo | Tipo | Obrigatório | Validação | Descrição |
|-------|------|-------------|-----------|-----------|
| `id` | integer | ✅ | id > 0 | ID único |
| `nome` | string | ✅ | 1-200 chars, único | Nome do grimório |
| `descricao` | string | ❌ | max 1000 chars | Descrição |
| `criado_em` | datetime | ✅ | ISO 8601 UTC | Data criação (auto) |
| `atualizado_em` | datetime | ✅ | ISO 8601 UTC | Data atualização (auto) |
| `total_feiticos` | integer | ✅ | >= 0 | Total de feitiços neste grimório |

---

### 3. Resposta Paginada

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
      "criado_em": "2026-01-26T10:00:00Z",
      "atualizado_em": "2026-01-26T10:00:00Z"
    }
  ],
  "total": 150,
  "pagina": 1,
  "por_pagina": 20,
  "total_paginas": 8,
  "sucesso": true,
  "mensagem": "Feitiços recuperados com sucesso",
  "timestamp": "2026-01-26T10:00:00Z"
}
```

#### Campos Detalhados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `itens` | array | Array de objetos (feitiços, grimórios, etc) |
| `total` | integer | Total de itens na coleção |
| `pagina` | integer | Página atual (começa em 1) |
| `por_pagina` | integer | Itens por página |
| `total_paginas` | integer | Total de páginas |
| `sucesso` | boolean | Indica sucesso da operação |
| `mensagem` | string | Mensagem descritiva |
| `timestamp` | datetime | ISO 8601 UTC da resposta |

---

### 4. Resposta Simples

```json
{
  "sucesso": true,
  "dados": {
    "id": 1,
    "nome": "Fireball",
    "nivel": 3
  },
  "mensagem": "Operação realizada com sucesso",
  "codigo": 200,
  "timestamp": "2026-01-26T10:00:00Z"
}
```

#### Campos Detalhados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `sucesso` | boolean | Indica sucesso |
| `dados` | object/array | Dados da resposta |
| `mensagem` | string | Mensagem descritiva |
| `codigo` | integer | Código HTTP |
| `timestamp` | datetime | ISO 8601 UTC |

---

### 5. Resposta de Erro

```json
{
  "sucesso": false,
  "dados": null,
  "mensagem": "Feitiço com ID 999 não encontrado",
  "codigo": 404,
  "timestamp": "2026-01-26T10:00:00Z"
}
```

#### Códigos de Erro

| Código | Significado | Exemplo |
|--------|------------|---------|
| 400 | Bad Request | Dados de entrada inválidos |
| 404 | Not Found | Recurso não encontrado |
| 409 | Conflict | Feitiço já existe |
| 422 | Unprocessable Entity | Validação falhou |
| 500 | Internal Server Error | Erro no servidor |

---

### 6. Estatísticas

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
      "5": 10,
      "6": 10,
      "7": 8,
      "8": 2
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
  "timestamp": "2026-01-26T10:00:00Z"
}
```

---

## Respostas Padrão

### Sucesso (200 OK)

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

```json
{
  "sucesso": true,
  "dados": {...},
  "mensagem": "Operação realizada com sucesso",
  "codigo": 200,
  "timestamp": "2026-01-26T10:00:00Z"
}
```

### Criado (201 Created)

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/v1/feiticos/1
```

```json
{
  "id": 1,
  "nome": "Fireball",
  ...
}
```

### Sem Conteúdo (204 No Content)

```http
HTTP/1.1 204 No Content
```

(Sem body)

### Erro de Validação (400/422)

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json
```

```json
{
  "sucesso": false,
  "dados": null,
  "mensagem": "Validação falhou: nome deve ter no máximo 100 caracteres",
  "codigo": 400,
  "timestamp": "2026-01-26T10:00:00Z"
}
```

### Não Encontrado (404)

```http
HTTP/1.1 404 Not Found
Content-Type: application/json
```

```json
{
  "sucesso": false,
  "dados": null,
  "mensagem": "Feitiço com ID 999 não encontrado",
  "codigo": 404,
  "timestamp": "2026-01-26T10:00:00Z"
}
```

### Conflito (409)

```http
HTTP/1.1 409 Conflict
Content-Type: application/json
```

```json
{
  "sucesso": false,
  "dados": null,
  "mensagem": "Feitiço 'Fireball' já existe",
  "codigo": 409,
  "timestamp": "2026-01-26T10:00:00Z"
}
```

---

## Validações

### Feitiço - Criação (POST)

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

**Validações:**
- ✅ `nome`: obrigatório, 1-100 chars, único
- ❌ `nivel`: 0-9 (opcional)
- ❌ `escola`: max 100 chars, deve estar em lista válida (opcional)
- ❌ `tempo`: max 100 chars (opcional)
- ❌ `alcance`: max 100 chars (opcional)
- ❌ `componentes`: max 500 chars (opcional)
- ❌ `duracao`: max 100 chars (opcional)
- ❌ `descricao`: max 5000 chars (opcional)

### Feitiço - Atualização (PUT)

```json
{
  "nivel": 2,
  "descricao": "Descrição atualizada..."
}
```

**Validações:**
- Todos os campos são opcionais
- Mesmas regras de comprimento da criação
- Não permite alterar `nome` (chave única)

---

## Exemplos

### ✅ Criar Feitiço

**Request:**
```http
POST /api/v1/feiticos
Content-Type: application/json

{
  "nome": "Fireball",
  "nivel": 3,
  "escola": "Evocação",
  "tempo": "1 ação",
  "alcance": "150 pés",
  "componentes": "V, S, M",
  "duracao": "Instantânea",
  "descricao": "Uma bola de fogo explode em um ponto à sua escolha dentro do alcance."
}
```

**Response (201):**
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
  "descricao": "Uma bola de fogo explode em um ponto à sua escolha dentro do alcance.",
  "criado_em": "2026-01-26T10:30:00Z",
  "atualizado_em": "2026-01-26T10:30:00Z"
}
```

---

### ✅ Listar Feitiços

**Request:**
```http
GET /api/v1/feiticos?skip=0&limit=20&ordem=nome
```

**Response (200):**
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
      "criado_em": "2026-01-26T10:30:00Z",
      "atualizado_em": "2026-01-26T10:30:00Z"
    }
  ],
  "total": 150,
  "pagina": 1,
  "por_pagina": 20,
  "total_paginas": 8,
  "sucesso": true,
  "mensagem": "Feitiços recuperados com sucesso",
  "timestamp": "2026-01-26T10:31:00Z"
}
```

---

### ✅ Buscar Feitiço

**Request:**
```http
GET /api/v1/feiticos/1
```

**Response (200):**
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
  "criado_em": "2026-01-26T10:30:00Z",
  "atualizado_em": "2026-01-26T10:30:00Z"
}
```

---

### ✅ Atualizar Feitiço

**Request:**
```http
PUT /api/v1/feiticos/1
Content-Type: application/json

{
  "nivel": 4,
  "descricao": "Versão melhorada da descrição..."
}
```

**Response (200):**
```json
{
  "id": 1,
  "nome": "Fireball",
  "nivel": 4,
  "escola": "Evocação",
  "tempo": "1 ação",
  "alcance": "150 pés",
  "componentes": "V, S, M",
  "duracao": "Instantânea",
  "descricao": "Versão melhorada da descrição...",
  "criado_em": "2026-01-26T10:30:00Z",
  "atualizado_em": "2026-01-26T10:35:00Z"
}
```

---

### ✅ Deletar Feitiço

**Request:**
```http
DELETE /api/v1/feiticos/1
```

**Response (204):**
```
(sem conteúdo)
```

---

### ✅ Obter Estatísticas

**Request:**
```http
GET /api/v1/grimorio/stats
```

**Response (200):**
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
      "Ilusão": 25
    }
  },
  "mensagem": "Estatísticas recuperadas com sucesso",
  "codigo": 200,
  "timestamp": "2026-01-26T10:36:00Z"
}
```

---

### ❌ Erro - Feitiço Não Encontrado

**Request:**
```http
GET /api/v1/feiticos/999
```

**Response (404):**
```json
{
  "sucesso": false,
  "dados": null,
  "mensagem": "Feitiço com ID 999 não encontrado",
  "codigo": 404,
  "timestamp": "2026-01-26T10:37:00Z"
}
```

---

### ❌ Erro - Feitiço Já Existe

**Request:**
```http
POST /api/v1/feiticos
Content-Type: application/json

{
  "nome": "Fireball",
  "nivel": 3,
  "escola": "Evocação"
}
```

**Response (409):**
```json
{
  "sucesso": false,
  "dados": null,
  "mensagem": "Feitiço 'Fireball' já existe",
  "codigo": 409,
  "timestamp": "2026-01-26T10:38:00Z"
}
```

---

## 📐 Formato de Datas

Todas as datas usam o formato **ISO 8601** com timezone UTC:

```
2026-01-26T10:30:00Z
2026-01-26T10:30:00.123456Z
```

**Parsing:**
```javascript
// JavaScript
const data = new Date('2026-01-26T10:30:00Z');

// Python
from datetime import datetime
data = datetime.fromisoformat('2026-01-26T10:30:00Z')
```

---

## 📝 Codificação

- **Charset**: UTF-8
- **Content-Type**: `application/json; charset=utf-8`
- **Line Ending**: `\n` (LF)

---

## 🔗 Referências

- [RFC 7231 - HTTP/1.1 Status Codes](https://tools.ietf.org/html/rfc7231)
- [RFC 8259 - JSON Data Interchange Format](https://tools.ietf.org/html/rfc8259)
- [ISO 8601 - Date and time format](https://en.wikipedia.org/wiki/ISO_8601)
- [OpenAPI 3.0 Specification](https://spec.openapis.org/oas/v3.0.3)

---

## 📄 Versão

**Contrato de Dados v2.0** - 26 de Janeiro de 2026
