import React from 'react';
import FeiticoList from './components/FeiticoList';
import FeiticoForm from './components/FeiticoForm';
import Stats from './components/Stats';

function App() {
  const [secaoAtiva, setSecaoAtiva] = React.useState('lista');

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-purple-800 to-blue-900">
      {/* Header */}
      <header className="bg-black bg-opacity-50 text-white">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold">📜 Grimório Mágico</h1>
            <p className="text-purple-200">Gerenciador de Feitiços v2.0</p>
          </div>
          <nav className="flex gap-4">
            <button
              onClick={() => setSecaoAtiva('lista')}
              className={`px-4 py-2 rounded ${
                secaoAtiva === 'lista'
                  ? 'bg-purple-600 text-white'
                  : 'bg-gray-700 hover:bg-gray-600'
              }`}
            >
              📚 Feitiços
            </button>
            <button
              onClick={() => setSecaoAtiva('novo')}
              className={`px-4 py-2 rounded ${
                secaoAtiva === 'novo'
                  ? 'bg-purple-600 text-white'
                  : 'bg-gray-700 hover:bg-gray-600'
              }`}
            >
              ➕ Novo
            </button>
            <button
              onClick={() => setSecaoAtiva('stats')}
              className={`px-4 py-2 rounded ${
                secaoAtiva === 'stats'
                  ? 'bg-purple-600 text-white'
                  : 'bg-gray-700 hover:bg-gray-600'
              }`}
            >
              📊 Estatísticas
            </button>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="min-h-screen py-8">
        {secaoAtiva === 'lista' && <FeiticoList />}
        {secaoAtiva === 'novo' && (
          <div className="max-w-2xl mx-auto px-6">
            <FeiticoForm onSucesso={() => setSecaoAtiva('lista')} />
          </div>
        )}
        {secaoAtiva === 'stats' && (
          <div className="max-w-6xl mx-auto px-6">
            <Stats />
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-black bg-opacity-50 text-white text-center py-4 mt-8">
        <p>Grimório Mágico v2.0 • API REST + React + FastAPI</p>
      </footer>
    </div>
  );
}

export default App;
