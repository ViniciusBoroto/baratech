from abc import ABC, abstractmethod

from core.domain.models.components import *


class CpuRepository(ABC):
    @abstractmethod
    def get_all_by_budget(self, budget: float) -> list[Cpu]:
        pass

class MotherboardRepository(ABC):
    @abstractmethod
    def get_all_by_budget(self, budget: float) -> list[MotherboardCategory]:
        pass

class RamRepository(ABC):
    @abstractmethod
    def get_all_by_budget(self, budget: float) -> list[RamCategory]:
        pass