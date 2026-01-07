from core.domain.models import *
from typing import List

from core.domain.models.machine_config import MachineConfig
from core.domain.models.machine_focus import MachineFocus
from core.domain.ports.repositories import *


class GenerateConfigUseCase:
    def __init__(self, cpu_repo: CpuRepository, mobo_repo: MotherboardRepository, ram_repo: RamRepository) -> None:
        self.cpu_repo = cpu_repo
        self.mobo_repo = mobo_repo
        self.ram_repo = ram_repo
    
    def _get_processing_kits(self, maximum_budget: float, focus: MachineFocus) -> List[ProcessingKit]:
        cpus = self.cpu_repo.get_all_by_budget(maximum_budget) 
        mobos = self.mobo_repo.get_all_by_budget(maximum_budget)
        rams = self.ram_repo.get_all_by_budget(maximum_budget)

        kits = []
        for cpu in cpus:
            for mobo in mobos:
                if cpu.price + mobo.average_price > maximum_budget:
                    continue
                if not mobo.accepts_cpu(cpu):
                    continue
                for ram in rams:
                    if not mobo.accepts_ram(ram):
                        continue
                    if cpu.price + mobo.average_price + ram.average_price > maximum_budget:
                        continue
                    if not mobo.accepts_ram(ram):
                        continue
                    kits.append(ProcessingKit(cpu=cpu, motherboard=mobo, ram=ram))
        return kits
    
    def _filter_best_kit(self, kits: List[ProcessingKit]) -> ProcessingKit:
        return max(kits, key=lambda k: k.cpu.score)

    def execute(self, budget: float, focus: MachineFocus) -> MachineConfig:
        kits = self._get_processing_kits(maximum_budget=budget, focus=focus)
        kit = self._filter_best_kit(kits) 
        return MachineConfig(processingKit=ProcessingKit(cpu=kit.cpu, motherboard=kit.motherboard, ram=kit.ram))
    