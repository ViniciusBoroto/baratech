from core.domain.components import *
from src.core.domain.machine_config import MachineConfig
from src.core.domain.machine_focus import MachineFocus
from src.core.domain.budget_allocation import BudgetAllocationStrategy
from src.core.domain.component_repository import ComponentRepository
from src.core.infra.in_memory_component_repository import InMemoryComponentRepository


class GenerateConfigUseCase:
    def __init__(self) -> None:
        return
    
    def execute(self, budget: float, focus: MachineFocus) -> MachineConfig:
        cpus = self.cpu_repo.get_cpus()

        cpu = Cpu(name="good ddr4 cpu", ddr=4, score=1200,socket="1", hasGraphics=False, price=1500)
        mobo = Motherboard(ddr=4, socket="1", name="good ddr4 mobo", price=500, score=300)
        gpu = Gpu(name="good gpu", score=1200, price=1500)
        ram = Ram(name="8gb ddr4", ddr=4, frequency=3200, price=200, gbCapacity=8, score=8*3200)

        return MachineConfig(cpu=cpu, motherboard=mobo, gpu=gpu, ram=[ram], storage=[], powerSupply=None, case=None)
    