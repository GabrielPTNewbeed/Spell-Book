# Grimório Mágico - Frontend Web

Frontend moderno construído com **React 18** + **Vite** + **Tailwind CSS** para gerenciar feitiços através de uma API REST.

## ✨ Features

- ✅ Interface responsiva e moderna
- ✅ Busca e filtros em tempo real
- ✅ Paginação inteligente
- ✅ Formulário de criação/edição de feitiços
- ✅ Estatísticas visuais
- ✅ Integração com API FastAPI
- ✅ Design com Tailwind CSS
- ✅ Hot reload em desenvolvimento

## 🚀 Quick Start

### 1. Instalação

```bash
# Entrar no diretório do frontend
cd frontend

# Instalar dependências
npm install
```

### 2. Executar em Desenvolvimento

```bash
npm run dev
```

A aplicação abrirá automaticamente em: **http://localhost:5173**

### 3. Build para Produção

```bash
npm run build
npm run preview
```

---

## 📁 Estrutura do Projeto

```
frontend/
├── src/
│   ├── components/
│   │   ├── FeiticoList.jsx      # Lista de feitiços
│   │   ├── FeiticoForm.jsx      # Formulário de criação/edição
│   │   └── Stats.jsx            # Estatísticas
│   ├── services/
│   │   └── api.js               # Cliente HTTP
│   ├── App.jsx                  # Componente principal
│   ├── main.jsx                 # Entrada
│   └── index.css                # Estilos globais
├── public/                      # Assets estáticos
├── index.html                   # Template HTML
├── package.json                 # Dependências
├── vite.config.js              # Configuração Vite
├── tailwind.config.js          # Configuração Tailwind
├── postcss.config.js           # Configuração PostCSS
└── README.md                    # Este arquivo
```

---

## 🔌 Integração com API

A aplicação se conecta à API em: `http://localhost:8000/api/v1`

Você pode alterar a URL base no arquivo `.env`:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

---

## 📦 Dependências Principais

- **React** - Framework UI
- **Vite** - Build tool e dev server
- **Axios** - Cliente HTTP
- **Tailwind CSS** - Framework CSS
- **React Router** - Roteamento (optional)

---

## 🎨 Componentes

### FeiticoList
Lista todos os feitiços com:
- Paginação
- Ordenação (nome, nível, recente)
- Ajuste de limite por página
- Cards informativos

### FeiticoForm
Formulário para criar/editar feitiços:
- Validação de campos
- Seleção de escola
- Feedback de sucesso/erro

### Stats
Exibe estatísticas do grimório:
- Total de feitiços
- Feitiços por nível
- Feitiços por escola
- Gráficos visuais

---

## 🚀 Exemplos de Uso

### Listar Feitiços
```javascript
import { feiticoService } from './services/api';

const { data } = await feiticoService.listar(0, 20, 'nome');
console.log(data.itens);
```

### Criar Feitiço
```javascript
const novoFeitico = {
  nome: 'Fireball',
  nivel: 3,
  escola: 'Evocação',
  tempo: '1 ação',
  alcance: '150 pés',
  componentes: 'V, S, M',
  duracao: 'Instantânea',
  descricao: 'Uma bola de fogo explode...'
};

await feiticoService.criar(novoFeitico);
```

### Buscar Feitiços
```javascript
const { data } = await feiticoService.buscar('fireball');
```

### Filtrar por Escola
```javascript
const { data } = await feiticoService.filtrarPorEscola('Evocação');
```

---

## 🎯 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_APP_NAME=Grimório Mágico
```

---

## 🧪 Testes

```bash
# (Adicionar testes com Vitest)
npm run test
```

---

## 🚢 Deploy

### Vercel
```bash
npm install -g vercel
vercel
```

### GitHub Pages
```bash
npm run build
# Configurar deploy em Settings > Pages
```

### Railway/Render
```bash
npm run build
# Fazer upload da pasta `dist/`
```

### Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "preview"]
```

---

## 🐛 Troubleshooting

### CORS Error
- Certifique-se que a API tem CORS configurado
- Verifique a URL da API em `services/api.js`

### Porta já em uso
```bash
npm run dev -- --port 5174
```

### Node modules problema
```bash
rm -rf node_modules package-lock.json
npm install
```

---

## 📚 Recursos

- [React Docs](https://react.dev/)
- [Vite Docs](https://vitejs.dev/)
- [Tailwind CSS Docs](https://tailwindcss.com/)
- [Axios Docs](https://axios-http.com/)

---

## 📄 Licença

MIT

---

## 🤝 Contribuições

Pull requests são bem-vindos!

```bash
git checkout -b feature/nova-feature
git commit -am 'Add nova feature'
git push origin feature/nova-feature
```
