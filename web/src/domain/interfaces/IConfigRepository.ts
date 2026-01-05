import { ComputerConfig, ConfigRequest } from '../../types';

// Interface que define o contrato para buscar configurações
// Seguindo o Dependency Inversion Principle
export interface IConfigRepository {
  getConfiguration(request: ConfigRequest): Promise<ComputerConfig>;
}
