import type { ComputerConfig, ConfigRequest } from "../../types";
import type { IConfigRepository } from "../../domain/interfaces/IConfigRepository";

// Implementação mock do repositório
// Em produção, isso fará chamadas HTTP reais para o backend
export class ConfigRepository implements IConfigRepository {
  private readonly baseUrl =
    import.meta.env.VITE_API_URL || "http://localhost:3000/api";

  async getConfiguration(request: ConfigRequest): Promise<ComputerConfig> {
    // TODO: Substituir por chamada real quando o backend estiver pronto
    // const response = await fetch(`${this.baseUrl}/config`, {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(request),
    // });
    // return await response.json();

    // Mock temporário para desenvolvimento
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({
          id: Math.random().toString(36).substr(2, 9),
          cpu: "AMD Ryzen 5 5600X",
          gpu: "NVIDIA RTX 3060",
          ram: "16GB DDR4 3200MHz",
          storage: "500GB NVMe SSD",
          motherboard: "B550M",
          powerSupply: "600W 80+ Bronze",
          case: "Mid Tower ATX",
          totalPrice: request.budget * 0.95,
          performance: {
            gaming: 85,
            productivity: 75,
            rendering: 70,
          },
        });
      }, 1500);
    });
  }
}
