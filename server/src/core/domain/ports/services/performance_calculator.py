from abc import ABC, abstractmethod

from core.domain.models.components import Cpu, Gpu
from core.domain.models.machine_config import MachineConfig
from core.domain.models.machine_focus import MachineFocus



class PerformanceCalculatorPort(ABC):
    def __init__(self,cpu_reference: int, gpu_reference: int):
        self.cpu_reference = cpu_reference
        self.gpu_reference = gpu_reference
        
    @abstractmethod
    def total_performance(self, machine_config: MachineConfig, focus: MachineFocus) -> int:
        pass
    @abstractmethod
    def cpu(self, cpu: Cpu) -> int:
        pass
    @abstractmethod
    def gpu(self, gpu: Gpu) -> int:
        pass

