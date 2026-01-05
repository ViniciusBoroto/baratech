import { ComputerConfig } from '../../../types';

interface ConfigResultProps {
  config: ComputerConfig;
  onReset: () => void;
}

export const ConfigResult = ({ config, onReset }: ConfigResultProps) => {
  const components = [
    { label: 'Processador', value: config.cpu, icon: '🔲' },
    { label: 'Placa de Vídeo', value: config.gpu, icon: '🎨' },
    { label: 'Memória RAM', value: config.ram, icon: '💾' },
    { label: 'Armazenamento', value: config.storage, icon: '💿' },
    { label: 'Placa-Mãe', value: config.motherboard, icon: '🔧' },
    { label: 'Fonte', value: config.powerSupply, icon: '⚡' },
    { label: 'Gabinete', value: config.case, icon: '📦' },
  ];

  const performanceMetrics = [
    { label: 'Gaming', value: config.performance.gaming, color: 'bg-green-500' },
    { label: 'Produtividade', value: config.performance.productivity, color: 'bg-blue-500' },
    { label: 'Renderização', value: config.performance.rendering, color: 'bg-purple-500' },
  ];

  return (
    <div className="w-full max-w-4xl mx-auto space-y-6">
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg p-6 text-center">
        <h2 className="text-2xl font-bold text-white mb-2">Configuração Gerada</h2>
        <p className="text-3xl font-bold text-white">
          R$ {config.totalPrice.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}
        </p>
      </div>

      <div className="bg-gray-800 rounded-lg p-6 space-y-4">
        <h3 className="text-lg font-semibold text-white mb-4">Componentes</h3>
        {components.map((component) => (
          <div key={component.label} className="flex items-start gap-3 p-3 bg-gray-900 rounded-lg">
            <span className="text-2xl">{component.icon}</span>
            <div className="flex-1">
              <p className="text-sm text-gray-400">{component.label}</p>
              <p className="text-white font-medium">{component.value}</p>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-gray-800 rounded-lg p-6 space-y-4">
        <h3 className="text-lg font-semibold text-white mb-4">Performance Estimada</h3>
        {performanceMetrics.map((metric) => (
          <div key={metric.label} className="space-y-2">
            <div className="flex justify-between text-sm">
              <span className="text-gray-400">{metric.label}</span>
              <span className="text-white font-medium">{metric.value}%</span>
            </div>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div
                className={`${metric.color} h-2 rounded-full transition-all duration-500`}
                style={{ width: `${metric.value}%` }}
              />
            </div>
          </div>
        ))}
      </div>

      <button
        onClick={onReset}
        className="w-full py-4 bg-gray-700 hover:bg-gray-600 text-white font-medium rounded-lg transition-colors"
      >
        Nova Configuração
      </button>
    </div>
  );
};
