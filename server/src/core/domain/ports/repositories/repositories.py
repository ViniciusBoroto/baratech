from abc import ABC, abstractmethod

from core.domain.models.components import *


class CpuRepositoryPort(ABC):
    @abstractmethod
    def get_all_by_budget(self, budget: float) -> list[Cpu]:
        pass

class MotherboardRepositoryPort(ABC):
    @abstractmethod
    def get_all_by_budget(self, budget: float) -> list[MotherboardCategory]:
        pass

class RamRepositoryPort(ABC):
    @abstractmethod
    def get_all_by_budget(self, budget: float) -> list[RamCategory]:
        pass

class GpuRepositoryPort(ABC):
    @abstractmethod
    def get_all_by_budget(self, budget: float) -> list[Gpu]:
        pass