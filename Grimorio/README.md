# 📜 Grimório Mágico v2.0 - Aplicação Web

Uma **aplicação web moderna** para gerenciar uma coleção de feitiços mágicos. Construída com **React** (frontend) e **FastAPI** (backend), com dados estruturados em **JSON REST**.

## 🚀 Quick Start

### **Opção 1: Docker Compose (Recomendado)**
```bash
docker-compose up -d
```

Acesse:
- 🌐 Frontend: http://localhost:5173
- 🔌 API: http://localhost:8000/api/v1
- 📚 Docs: http://localhost:8000/docs

### **Opção 2: Desenvolvimento Local**

**Terminal 1 - Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## 📚 Documentação

- **[README_WEB.md](README_WEB.md)** - Guia completo
- **[CONTRATO_DADOS.md](CONTRATO_DADOS.md)** - Especificação JSON
- **[GUIA_RAPIDO.md](GUIA_RAPIDO.md)** - Referência rápida
- **[backend/API.md](backend/API.md)** - Endpoints da API
- **[backend/README.md](backend/README.md)** - Setup backend
- **[frontend/README.md](frontend/README.md)** - Setup frontend
3. Procure por **Python** (ou selecione `python.exe`)
4. Marque ✓ **"Sempre usar este aplicativo"**
5. Clique OK

---

### ❌ Problema: "Python não encontrado"

**Verificar**:
```cmd
python --version
```

Se não funcionar:
1. Instale Python de: https://www.python.org/
2. Durante a instalação, **MARQUE**: ✓ "Add Python to PATH"
3. Reinicie o computador
4. Tente novamente

---

### ❌ Problema: "ModuleNotFoundError: PIL ou tkinter"

**Solução**:
```cmd
pip install pillow
```

**Tkinter** geralmente vem com Python, mas se faltar:
```cmd
python -m pip install tk
```

---

## 📁 Arquivos de Execução

| Arquivo | Tipo | Como Usar | Melhor Para |
|---------|------|-----------|------------|
| `iniciar_grimorio.bat` | Batch | Duplo clique | ✅ Windows |
| `grimorio_launcher.py` | Python | Duplo clique | ✅ Multiplataforma |
| `Grimorio.py` | Python | Terminal | Debug/Logs |
| `COMO_EXECUTAR.md` | Docs | Referência | Dúvidas técnicas |

---

## 🚀 Recomendação

**Para Windows**: Use **`iniciar_grimorio.bat`**

**Razões**:
- ✅ Abre direto sem terminal invisível
- ✅ Mostra mensagens de erro se houver
- ✅ Não depende de associações de arquivo
- ✅ Melhor compatibilidade

---

## 📝 O que Cada Arquivo Faz

### `iniciar_grimorio.bat`
- Arquivo batch do Windows
- Executa Python nesta pasta
- Abre janela de comando (pode fechar após)

### `grimorio_launcher.py`
- Script Python puro
- Inicializa o módulo principal
- Funciona em Windows, Linux, Mac

### `Grimorio.py`
- Aplicação principal
- Contém toda a lógica
- Gera logs em `logs/`

---

## 📊 Estrutura de Logs

Quando você executa o app, logs são criados automaticamente:

```
logs/
└── grimorio_20260125_142530.log
```

**Para ver logs**:
1. Abra a pasta `logs/`
2. Abra o arquivo `.log` com qualquer editor de texto

---

## 🎯 Próximas Execuções

1. **Primeira vez**: Use `iniciar_grimorio.bat`
2. **Crie um atalho**: Clique direito → Enviar para → Desktop
3. **Próximas vezes**: Duplo clique no atalho da área de trabalho

---

## ✅ Tudo Pronto!

A aplicação **Grimório Mágico** está pronta para usar. 🎭✨

**Dúvidas?** Abra um terminal e execute:
```cmd
python Grimorio.py
```
Assim você vê mensagens de erro detalhadas.
