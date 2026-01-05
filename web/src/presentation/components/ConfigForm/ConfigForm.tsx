import { useState } from "react";
import { ConfigRequest, MachineFocus } from "../../../types";
import { FcSportsMode, FcFilmReel, FcBriefcase, FcReading, FcVideoCall } from "react-icons/fc";

interface ConfigFormProps {
  onSubmit: (request: ConfigRequest) => void;
  loading: boolean;
}

const focusOptions = [
  {
    value: MachineFocus.COMPETITIVE_GAMING,
    label: "Jogos Competitivos",
    icon: FcSportsMode,
    description: "Alto FPS, resposta rápida",
  },
  {
    value: MachineFocus.STORY_GAMING,
    label: "Jogos de História",
    icon: FcFilmReel,
    description: "Gráficos imersivos",
  },
  {
    value: MachineFocus.WORK,
    label: "Trabalho",
    icon: FcBriefcase,
    description: "Multitarefa, produtividade",
  },
  {
    value: MachineFocus.STUDY,
    label: "Estudos",
    icon: FcReading,
    description: "Navegação, documentos",
  },
  {
    value: MachineFocus.VIDEO_EDITING,
    label: "Edição de Vídeo",
    icon: FcVideoCall,
    description: "Renderização, timeline",
  },
];

export const ConfigForm = ({ onSubmit, loading }: ConfigFormProps) => {
  const [budget, setBudget] = useState("");
  const [focus, setFocus] = useState<MachineFocus | "">("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (budget && focus) {
      onSubmit({ budget: Number(budget), focus: focus as MachineFocus });
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="w-full max-w-4xl mx-auto space-y-8"
    >
      <div className="space-y-3">
        <label className="block text-sm font-medium text-gray-300">
          Orçamento (R$)
        </label>
        <input
          type="number"
          value={budget}
          onChange={(e) => setBudget(e.target.value)}
          placeholder="Ex: 5000"
          min="1000"
          step="100"
          required
          disabled={loading}
          className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition disabled:opacity-50"
        />
        <p className="text-xs text-gray-500">Valor mínimo: R$ 1.000</p>
      </div>

      <div className="space-y-3">
        <label className="block text-sm font-medium text-gray-300">
          Foco da Máquina
        </label>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
          {focusOptions.map((option) => (
            <button
              key={option.value}
              type="button"
              onClick={() => setFocus(option.value)}
              disabled={loading}
              className={`p-4 rounded-lg border-2 transition-all text-left ${
                focus === option.value
                  ? "border-blue-500 bg-blue-500/10"
                  : "border-gray-700 bg-gray-800 hover:border-gray-600"
              } disabled:opacity-50`}
            >
              <div className="text-2xl mb-2">
                <option.icon />
              </div>
              <div className="font-medium text-white">{option.label}</div>
              <div className="text-xs text-gray-400 mt-1">
                {option.description}
              </div>
            </button>
          ))}
        </div>
      </div>

      <button
        type="submit"
        disabled={loading || !budget || !focus}
        className="w-full py-4 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 disabled:cursor-not-allowed text-white font-medium rounded-lg transition-colors"
      >
        {loading ? "Gerando configuração..." : "Gerar Configuração"}
      </button>
    </form>
  );
};
