import { ConfigForm } from "../components/ConfigForm/ConfigForm";
import { ConfigResult } from "../components/ConfigResult/ConfigResult";
import { useConfig } from "../hooks/useConfig";
import { GetComputerConfigUseCase } from "../../application/use-cases/GetComputerConfigUseCase";
import { ConfigRepository } from "../../infrastructure/api/ConfigRepository";

const configRepository = new ConfigRepository();
const getConfigUseCase = new GetComputerConfigUseCase(configRepository);

export const HomePage = () => {
  const { config, loading, error, fetchConfig, reset } =
    useConfig(getConfigUseCase);

  return (
    <div className="min-h-screen bg-gray-900 py-12 px-4">
      <div className="max-w-6xl mx-auto">
        <header className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            BaraTech
          </h1>
          <p className="text-gray-400 text-lg">
            Configure seu PC ideal baseado no seu orçamento e necessidades
          </p>
        </header>

        {error && (
          <div className="max-w-4xl mx-auto mb-6 p-4 bg-red-500/10 border border-red-500 rounded-lg">
            <p className="text-red-500 text-center">{error}</p>
          </div>
        )}

        {!config ? (
          <ConfigForm onSubmit={fetchConfig} loading={loading} />
        ) : (
          <ConfigResult config={config} onReset={reset} />
        )}
      </div>
    </div>
  );
};
