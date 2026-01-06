from src.core.domain.machine_config import MachineConfig
from src.core.domain.machine_focus import MachineFocus
from src.core.domain.budget_allocation import BudgetAllocationStrategy
from src.core.domain.component_repository import ComponentRepository
from src.core.infra.in_memory_component_repository import InMemoryComponentRepository


class GenerateConfigUseCase:
    def __init__(self, component_repo: ComponentRepository = None) -> None:
        self.component_repo = component_repo or InMemoryComponentRepository()
    
    def execute(self, budget: float, focus: MachineFocus) -> MachineConfig:
        allocation = BudgetAllocationStrategy.get_allocation(focus, budget)
        
        # Select best components within allocated budgets
        cpu = self.component_repo.get_best_component_in_budget('cpu', allocation['cpu'])
        gpu = self.component_repo.get_best_component_in_budget('gpu', allocation['gpu'])
        ram = self.component_repo.get_best_component_in_budget('ram', allocation['ram'])
        storage = self.component_repo.get_best_component_in_budget('storage', allocation['storage'])
        motherboard = self.component_repo.get_best_component_in_budget('motherboard', allocation['motherboard'])
        power_supply = self.component_repo.get_best_component_in_budget('power_supply', allocation['power_supply'])
        case = self.component_repo.get_best_component_in_budget('case', allocation['case'])
        
        return MachineConfig(
            cpu=cpu.name,
            gpu=gpu.name,
            ram=ram.name,
            storage=storage.name,
            motherboard=motherboard.name,
            powerSupply=power_supply.name,
            case=case.name
        )
