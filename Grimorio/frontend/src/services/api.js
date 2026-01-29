import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Serviço de Feitiços
export const feiticoService = {
  // Listar todos os feitiços
  listar: (skip = 0, limit = 20, ordem = 'nome') => {
    return apiClient.get('/feiticos', {
      params: { skip, limit, ordem }
    });
  },

  // Obter um feitiço específico
  obter: (id) => {
    return apiClient.get(`/feiticos/${id}`);
  },

  // Criar novo feitiço
  criar: (dados) => {
    return apiClient.post('/feiticos', dados);
  },

  // Atualizar feitiço
  atualizar: (id, dados) => {
    return apiClient.put(`/feiticos/${id}`, dados);
  },

  // Deletar feitiço
  deletar: (id) => {
    return apiClient.delete(`/feiticos/${id}`);
  },

  // Buscar por nome
  buscar: (termo, skip = 0, limit = 20) => {
    return apiClient.get('/feiticos/buscar', {
      params: { termo, skip, limit }
    });
  },

  // Filtrar por escola
  filtrarPorEscola: (escola, skip = 0, limit = 20) => {
    return apiClient.get('/feiticos/escola', {
      params: { escola, skip, limit }
    });
  },

  // Filtrar por nível
  filtrarPorNivel: (nivel, skip = 0, limit = 20) => {
    return apiClient.get('/feiticos/nivel', {
      params: { nivel, skip, limit }
    });
  },
};

// Serviço de Grimório
export const grimorioService = {
  // Obter informações do grimório
  obterInfo: () => {
    return apiClient.get('/grimorio');
  },

  // Obter estatísticas
  obterStats: () => {
    return apiClient.get('/grimorio/stats');
  },
};

export default apiClient;
