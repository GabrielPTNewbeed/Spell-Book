import React, { useState, useEffect } from 'react';
import { feiticoService } from '../services/api';

export default function FeiticoList() {
  const [feiticos, setFeiticos] = useState([]);
  const [total, setTotal] = useState(0);
  const [pagina, setPagina] = useState(1);
  const [limite, setLimite] = useState(20);
  const [carregando, setCarregando] = useState(false);
  const [erro, setErro] = useState(null);
  const [ordem, setOrdem] = useState('nome');

  useEffect(() => {
    carregarFeiticos();
  }, [pagina, limite, ordem]);

  const carregarFeiticos = async () => {
    setCarregando(true);
    setErro(null);
    try {
      const skip = (pagina - 1) * limite;
      const response = await feiticoService.listar(skip, limite, ordem);
      setFeiticos(response.data.itens);
      setTotal(response.data.total);
    } catch (err) {
      setErro('Erro ao carregar feitiços: ' + err.message);
      console.error(err);
    } finally {
      setCarregando(false);
    }
  };

  const totalPaginas = Math.ceil(total / limite);

  return (
    <div className="max-w-6xl mx-auto p-6">
      <h1 className="text-4xl font-bold mb-8 text-purple-900">📜 Grimório Mágico</h1>

      {erro && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {erro}
        </div>
      )}

      {/* Controles */}
      <div className="mb-6 flex gap-4 flex-wrap">
        <select
          value={ordem}
          onChange={(e) => {
            setOrdem(e.target.value);
            setPagina(1);
          }}
          className="px-4 py-2 border border-gray-300 rounded bg-white"
        >
          <option value="nome">Ordenar por Nome</option>
          <option value="nivel">Ordenar por Nível</option>
          <option value="recente">Mais Recentes</option>
        </select>

        <select
          value={limite}
          onChange={(e) => {
            setLimite(parseInt(e.target.value));
            setPagina(1);
          }}
          className="px-4 py-2 border border-gray-300 rounded bg-white"
        >
          <option value={10}>10 por página</option>
          <option value={20}>20 por página</option>
          <option value={50}>50 por página</option>
        </select>

        <span className="px-4 py-2 text-gray-600">
          Total: {total} feitiços
        </span>
      </div>

      {/* Lista de Feitiços */}
      {carregando ? (
        <div className="text-center py-8">
          <div className="inline-block animate-spin">⚡</div>
          <p className="mt-2">Carregando feitiços...</p>
        </div>
      ) : feiticos.length > 0 ? (
        <>
          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {feiticos.map((feitico) => (
              <div
                key={feitico.id}
                className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow p-4 border-l-4 border-purple-600"
              >
                <h3 className="text-xl font-bold text-gray-900 mb-2">
                  {feitico.nome}
                </h3>
                
                <div className="space-y-1 text-sm">
                  <p>
                    <span className="font-semibold">Nível:</span>{' '}
                    <span className="bg-purple-100 px-2 py-1 rounded">
                      {feitico.nivel || 'Cantrip'}
                    </span>
                  </p>
                  
                  {feitico.escola && (
                    <p>
                      <span className="font-semibold">Escola:</span> {feitico.escola}
                    </p>
                  )}
                  
                  {feitico.tempo && (
                    <p>
                      <span className="font-semibold">Tempo:</span> {feitico.tempo}
                    </p>
                  )}
                  
                  {feitico.alcance && (
                    <p>
                      <span className="font-semibold">Alcance:</span> {feitico.alcance}
                    </p>
                  )}
                  
                  {feitico.componentes && (
                    <p>
                      <span className="font-semibold">Componentes:</span> {feitico.componentes}
                    </p>
                  )}
                  
                  {feitico.duracao && (
                    <p>
                      <span className="font-semibold">Duração:</span> {feitico.duracao}
                    </p>
                  )}
                </div>

                {feitico.descricao && (
                  <p className="mt-3 text-gray-700 text-sm line-clamp-2">
                    {feitico.descricao}
                  </p>
                )}

                <div className="mt-4 flex gap-2">
                  <button className="flex-1 bg-blue-500 hover:bg-blue-600 text-white py-1 rounded text-sm">
                    Editar
                  </button>
                  <button className="flex-1 bg-red-500 hover:bg-red-600 text-white py-1 rounded text-sm">
                    Deletar
                  </button>
                </div>
              </div>
            ))}
          </div>

          {/* Paginação */}
          <div className="mt-8 flex justify-center items-center gap-4">
            <button
              onClick={() => setPagina(p => Math.max(1, p - 1))}
              disabled={pagina === 1}
              className="px-4 py-2 bg-purple-600 text-white rounded disabled:opacity-50 disabled:cursor-not-allowed hover:bg-purple-700"
            >
              ← Anterior
            </button>

            <span className="px-4 py-2">
              Página {pagina} de {totalPaginas}
            </span>

            <button
              onClick={() => setPagina(p => Math.min(totalPaginas, p + 1))}
              disabled={pagina === totalPaginas}
              className="px-4 py-2 bg-purple-600 text-white rounded disabled:opacity-50 disabled:cursor-not-allowed hover:bg-purple-700"
            >
              Próxima →
            </button>
          </div>
        </>
      ) : (
        <div className="text-center py-8">
          <p className="text-gray-500">Nenhum feitiço encontrado</p>
        </div>
      )}
    </div>
  );
}
