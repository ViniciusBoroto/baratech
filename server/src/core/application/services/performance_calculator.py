from abc import ABC, abstractmethod

from core.domain.models.components import Cpu, Gpu
from core.domain.models.machine_config import MachineConfig
from core.domain.models.machine_focus import MachineFocus
from core.domain.ports.services.performance_calculator import PerformanceCalculatorPort




class PerformanceCalculator(PerformanceCalculatorPort):
    def __init__(self,cpu_reference: int, gpu_reference: int):
        super().__init__(cpu_reference, gpu_reference)
        
    @abstractmethod
    def total_performance(self, machine_config: MachineConfig, focus: MachineFocus) -> int:
        pass
    @abstractmethod
    def cpu(self, cpu: Cpu) -> int:
        pass
    @abstractmethod
    def gpu(self, gpu: Gpu) -> int:
        pass

