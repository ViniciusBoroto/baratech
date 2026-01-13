from core.domain.models import *
from typing import List

from core.domain.models.machine_config import MachineConfig
from core.domain.models.machine_focus import MachineFocus
from core.domain.ports.repositories import *


class GenerateConfigUseCase:
    def __init__(self, cpu_repo: CpuRepositoryPort, mobo_repo: MotherboardRepositoryPort, ram_repo: RamRepositoryPort, gpu_repo: GpuRepositoryPort) -> None:
        self.cpu_repo = cpu_repo
        self.mobo_repo = mobo_repo
        self.ram_repo = ram_repo
        self.gpu_repo = gpu_repo
    
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

    def _combine_processing_kits_with_gpus(self, kits: list[ProcessingKit], gpus: list[Gpu], budget: float) -> list[MachineConfig]:
            cfgs =[]
            for kit in kits:
                if kit.cpu.apu_score:
                    cfgs.append(MachineConfig(processingKit=kit))
                for gpu in gpus:
                    if gpu.price + kit.average_price() <= budget:
                        cfgs.append(MachineConfig(processingKit=kit, gpu=gpu))

            return cfgs
    def _get_most_performatic_config(self, configs: list[MachineConfig]) -> MachineConfig:
        return max(configs, key=lambda c: c.total_cost())

    def execute(self, budget: float, focus: MachineFocus) -> MachineConfig:
        kits = self._get_processing_kits(maximum_budget=budget, focus=focus)
        kit = self._filter_best_kit(kits) 
        if not kit:
            raise Exception("No kit found")
        
        gpus = self.gpu_repo.get_all_by_budget(budget)
        candidates = self._combine_processing_kits_with_gpus(kits, gpus, budget)
        if not candidates:
            raise Exception("No config found")
        best = self._get_most_performatic_config(candidates)
        if not best:
            raise Exception("No config found")

        return best
    