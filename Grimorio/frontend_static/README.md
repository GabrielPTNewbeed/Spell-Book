# Grimório — Frontend estático para Vercel

Esta pasta contém uma versão frontend estática do Grimório pronta para deploy em Vercel ou GitHub Pages.

Arquivos:
- `index.html` — UI principal (HTML)
- `styles.css` — Estilos (CSS)
- `app.js` — Lógica (JS): armazenamento em `localStorage`, import/export JSON, geração caótica

Deploy rápido no Vercel:
1. Crie um repositório no GitHub e envie o conteúdo desta pasta.
2. No Vercel, clique em "New Project" → importe seu repositório.
3. Configure o root (se necessário) para a pasta `frontend_static`.
4. Vercel detecta site estático — clique em Deploy.

Uso local:
Abra `frontend_static/index.html` no navegador ou rode um servidor simples:

```bash
cd frontend_static
python -m http.server 5173
# então abra http://localhost:5173
```
