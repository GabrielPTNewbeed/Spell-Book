# Use imagem oficial do Node.js
FROM node:18-alpine

# Configurar diretório de trabalho
WORKDIR /app

# Copiar package.json e package-lock.json
COPY package*.json ./

# Instalar dependências
RUN npm ci

# Copiar código da aplicação
COPY . .

# Build da aplicação
RUN npm run build

# Expor porta
EXPOSE 5173

# Comando para iniciar a aplicação em desenvolvimento
CMD ["npm", "run", "dev", "--", "--host"]
