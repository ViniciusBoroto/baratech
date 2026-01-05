import { useState } from 'react';
import { ComputerConfig, ConfigRequest } from '../../types';
import { GetComputerConfigUseCase } from '../../application/use-cases/GetComputerConfigUseCase';

interface UseConfigState {
  config: ComputerConfig | null;
  loading: boolean;
  error: string | null;
  fetchConfig: (request: ConfigRequest) => Promise<void>;
  reset: () => void;
}

// Hook customizado para gerenciar o estado da configuração
export const useConfig = (useCase: GetComputerConfigUseCase): UseConfigState => {
  const [config, setConfig] = useState<ComputerConfig | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchConfig = async (request: ConfigRequest) => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await useCase.execute(request);
      setConfig(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro ao buscar configuração');
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setConfig(null);
    setError(null);
  };

  return { config, loading, error, fetchConfig, reset };
};
