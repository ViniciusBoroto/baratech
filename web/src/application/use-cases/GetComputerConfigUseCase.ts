import { ComputerConfig, ConfigRequest } from '../../types';
import { IConfigRepository } from '../../domain/interfaces/IConfigRepository';

// Caso de uso: Obter configuração de computador
// Segue o Single Responsibility Principle
export class GetComputerConfigUseCase {
  constructor(private configRepository: IConfigRepository) {}

  async execute(request: ConfigRequest): Promise<ComputerConfig> {
    return await this.configRepository.getConfiguration(request);
  }
}
