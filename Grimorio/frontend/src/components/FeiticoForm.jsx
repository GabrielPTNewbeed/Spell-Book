import React, { useState } from 'react';
import { feiticoService } from '../services/api';

export default function FeiticoForm({ onSucesso, feiticoEdicao = null }) {
  const [formData, setFormData] = useState(
    feiticoEdicao || {
      nome: '',
      nivel: 0,
      escola: '',
      tempo: '',
      alcance: '',
      componentes: '',
      duracao: '',
      descricao: '',
    }
  );

  const [carregando, setCarregando] = useState(false);
  const [erro, setErro] = useState(null);
  const [sucesso, setSucesso] = useState(false);

  const escolas = [
    'Abjuração',
    'Conjuração',
    'Divinação',
    'Encantamento',
    'Evocação',
    'Ilusão',
    'Necromancia',
    'Transmutação',
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === 'nivel' ? parseInt(value) : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setCarregando(true);
    setErro(null);
    setSucesso(false);

    try {
      if (feiticoEdicao) {
        await feiticoService.atualizar(feiticoEdicao.id, formData);
      } else {
        await feiticoService.criar(formData);
      }
      setSucesso(true);
      setFormData({
        nome: '',
        nivel: 0,
        escola: '',
        tempo: '',
        alcance: '',
        componentes: '',
        duracao: '',
        descricao: '',
      });
      if (onSucesso) onSucesso();
    } catch (err) {
      setErro('Erro ao salvar feitiço: ' + err.response?.data?.detail || err.message);
    } finally {
      setCarregando(false);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white rounded-lg shadow-md p-6 max-w-2xl mx-auto"
    >
      <h2 className="text-2xl font-bold mb-6">
        {feiticoEdicao ? '✏️ Editar Feitiço' : '➕ Novo Feitiço'}
      </h2>

      {erro && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {erro}
        </div>
      )}

      {sucesso && (
        <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4">
          Feitiço salvo com sucesso! ✨
        </div>
      )}

      <div className="grid grid-cols-2 gap-4 mb-4">
        <div className="col-span-2">
          <label className="block text-gray-700 font-semibold mb-2">
            Nome do Feitiço *
          </label>
          <input
            type="text"
            name="nome"
            value={formData.nome}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-purple-600"
            placeholder="Ex: Fireball"
          />
        </div>

        <div>
          <label className="block text-gray-700 font-semibold mb-2">
            Nível (0-9)
          </label>
          <input
            type="number"
            name="nivel"
            value={formData.nivel}
            onChange={handleChange}
            min="0"
            max="9"
            className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-purple-600"
          />
        </div>

        <div>
          <label className="block text-gray-700 font-semibold mb-2">
            Escola de Magia
          </label>
          <select
            name="escola"
            value={formData.escola}
            onChange={handleChange}
            className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-purple-600"
          >
            <option value="">Selecione...</option>
            {escolas.map((escola) => (
              <option key={escola} value={escola}>
                {escola}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-gray-700 font-semibold mb-2">
            Tempo de Conjuração
          </label>
          <input
            type="text"
            name="tempo"
            value={formData.tempo}
            onChange={handleChange}
            className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-purple-600"
            placeholder="Ex: 1 ação"
          />
        </div>

        <div>
          <label className="block text-gray-700 font-semibold mb-2">
            Alcance
          </label>
          <input
            type="text"
            name="alcance"
            value={formData.alcance}
            onChange={handleChange}
            className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-purple-600"
            placeholder="Ex: 150 pés"
          />
        </div>

        <div>
          <label className="block text-gray-700 font-semibold mb-2">
            Componentes
          </label>
          <input
            type="text"
            name="componentes"
            value={formData.componentes}
            onChange={handleChange}
            className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-purple-600"
            placeholder="Ex: V, S, M"
          />
        </div>

        <div className="col-span-2">
          <label className="block text-gray-700 font-semibold mb-2">
            Duração
          </label>
          <input
            type="text"
            name="duracao"
            value={formData.duracao}
            onChange={handleChange}
            className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-purple-600"
            placeholder="Ex: Instantânea"
          />
        </div>

        <div className="col-span-2">
          <label className="block text-gray-700 font-semibold mb-2">
            Descrição
          </label>
          <textarea
            name="descricao"
            value={formData.descricao}
            onChange={handleChange}
            rows="6"
            className="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-purple-600"
            placeholder="Descrição detalhada do feitiço..."
          />
        </div>
      </div>

      <div className="flex gap-4">
        <button
          type="submit"
          disabled={carregando}
          className="flex-1 bg-purple-600 hover:bg-purple-700 text-white font-semibold py-2 rounded disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {carregando ? 'Salvando...' : feiticoEdicao ? 'Atualizar' : 'Criar Feitiço'}
        </button>
        <button
          type="reset"
          className="flex-1 bg-gray-400 hover:bg-gray-500 text-white font-semibold py-2 rounded"
        >
          Limpar
        </button>
      </div>
    </form>
  );
}
