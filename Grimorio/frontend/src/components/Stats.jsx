import React, { useState, useEffect } from 'react';
import { grimorioService } from '../services/api';

export default function Stats() {
  const [stats, setStats] = useState(null);
  const [carregando, setCarregando] = useState(true);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    carregarStats();
  }, []);

  const carregarStats = async () => {
    try {
      const response = await grimorioService.obterStats();
      setStats(response.data.dados);
    } catch (err) {
      setErro('Erro ao carregar estatísticas: ' + err.message);
      console.error(err);
    } finally {
      setCarregando(false);
    }
  };

  if (carregando) {
    return <div className="text-center py-8">Carregando estatísticas...</div>;
  }

  if (erro) {
    return <div className="text-red-600">{erro}</div>;
  }

  if (!stats) {
    return <div className="text-gray-500">Nenhuma estatística disponível</div>;
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-6">📊 Estatísticas do Grimório</h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div className="bg-purple-100 rounded-lg p-4 border-l-4 border-purple-600">
          <p className="text-gray-600 text-sm font-semibold">Total de Feitiços</p>
          <p className="text-3xl font-bold text-purple-600">
            {stats.total_feiticos}
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Por Nível */}
        <div>
          <h3 className="text-xl font-semibold mb-4">Feitiços por Nível</h3>
          <div className="space-y-2">
            {Object.entries(stats.feiticos_por_nivel)
              .sort(([a], [b]) => parseInt(a) - parseInt(b))
              .map(([nivel, quantidade]) => (
                <div key={nivel} className="flex items-center">
                  <span className="w-20 font-semibold">
                    {nivel === '0' ? 'Cantrip' : `Nível ${nivel}`}
                  </span>
                  <div className="flex-1 bg-gray-200 rounded-full h-6 ml-4 relative">
                    <div
                      className="bg-purple-500 h-6 rounded-full flex items-center justify-center"
                      style={{
                        width: `${(quantidade / stats.total_feiticos) * 100}%`,
                      }}
                    >
                      {quantidade > 0 && (
                        <span className="text-white text-xs font-semibold">
                          {quantidade}
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              ))}
          </div>
        </div>

        {/* Por Escola */}
        <div>
          <h3 className="text-xl font-semibold mb-4">Feitiços por Escola</h3>
          <div className="space-y-2">
            {Object.entries(stats.feiticos_por_escola)
              .sort(([, a], [, b]) => b - a)
              .map(([escola, quantidade]) => (
                <div key={escola} className="flex items-center justify-between p-2 bg-gray-50 rounded">
                  <span className="font-medium">{escola}</span>
                  <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm font-semibold">
                    {quantidade}
                  </span>
                </div>
              ))}
          </div>
        </div>
      </div>
    </div>
  );
}
