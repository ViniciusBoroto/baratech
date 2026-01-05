// Entidade que representa uma configuração de computador
export interface ComputerConfig {
  id: string;
  cpu: string;
  gpu: string;
  ram: string;
  storage: string;
  motherboard: string;
  powerSupply: string;
  case: string;
  totalPrice: number;
  performance: {
    gaming: number;
    productivity: number;
    rendering: number;
  };
}

// Tipos de foco da máquina
export enum MachineFocus {
  COMPETITIVE_GAMING = 'competitive_gaming',
  STORY_GAMING = 'story_gaming',
  WORK = 'work',
  STUDY = 'study',
  VIDEO_EDITING = 'video_editing',
}

// Request para gerar configuração
export interface ConfigRequest {
  budget: number;
  focus: MachineFocus;
}
