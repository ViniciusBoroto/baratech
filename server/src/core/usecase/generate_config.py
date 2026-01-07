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
                if cpu.price + mobo.price > maximum_budget: continue
                if not mobo.accepts_cpu(cpu): continue
                for ram in rams:
                    if ram.ddr != mobo.ddr: continue
                    if cpu.price + mobo.price + ram.price > maximum_budget: continue
                    if not mobo.accepts_ram(ram): continue
                    kits.append(ProcessingKit(cpu=cpu, motherboard=mobo, ram=ram))
        return kits

    def execute(self, budget: float, focus: MachineFocus) -> MachineConfig:
        socket = "AM4"
        kits = self._get_processing_kits(maximum_budget=budget, focus=focus)

        cpu = Cpu(name="good ddr4 cpu", ddr=4, score=1200,socket=socket, hasGraphics=False, price=1500)
        mobo = MotherboardCategory(ddr=4, socket=socket,averagePrice=500)
        ram = RamCategory(ddr=4, frequency=3200, gbCapacity=16, averagePrice=200)
        gpu = Gpu(name="good gpu", score=1200, price=1500, vram=8, frequency=1800)

        return MachineConfig(gpu=gpu, processingKit=ProcessingKit(cpu=cpu, motherboard=mobo, ram=ram))
    