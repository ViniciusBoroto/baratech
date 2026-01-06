from typing import List
from server.src.core.domain.component import Component
from server.src.core.domain.component_repository import ComponentRepository

class InMemoryComponentRepository(ComponentRepository):
    def __init__(self):
        self.components = [
            # CPUs
            Component(name="AMD Ryzen 5 5600X", price=200, performance_score=85, specs={"cores": 6, "threads": 12}, category="cpu"),
            Component(name="AMD Ryzen 7 5800X", price=300, performance_score=90, specs={"cores": 8, "threads": 16}, category="cpu"),
            Component(name="Intel i5-12600K", price=250, performance_score=87, specs={"cores": 10, "threads": 16}, category="cpu"),
            Component(name="Intel i7-12700K", price=350, performance_score=92, specs={"cores": 12, "threads": 20}, category="cpu"),
            
            # GPUs
            Component(name="RTX 3060", price=400, performance_score=75, specs={"vram": "12GB", "cuda_cores": 3584}, category="gpu"),
            Component(name="RTX 3070", price=600, performance_score=85, specs={"vram": "8GB", "cuda_cores": 5888}, category="gpu"),
            Component(name="RTX 4060", price=450, performance_score=78, specs={"vram": "8GB", "cuda_cores": 3072}, category="gpu"),
            Component(name="RTX 4070", price=700, performance_score=88, specs={"vram": "12GB", "cuda_cores": 5888}, category="gpu"),
            
            # RAM
            Component(name="16GB DDR4-3200", price=80, performance_score=70, specs={"capacity": "16GB", "speed": "3200MHz"}, category="ram"),
            Component(name="32GB DDR4-3600", price=150, performance_score=85, specs={"capacity": "32GB", "speed": "3600MHz"}, category="ram"),
            Component(name="16GB DDR5-5600", price=120, performance_score=80, specs={"capacity": "16GB", "speed": "5600MHz"}, category="ram"),
            
            # Storage
            Component(name="1TB NVMe SSD", price=100, performance_score=80, specs={"capacity": "1TB", "type": "NVMe"}, category="storage"),
            Component(name="2TB NVMe SSD", price=180, performance_score=85, specs={"capacity": "2TB", "type": "NVMe"}, category="storage"),
            Component(name="500GB NVMe SSD", price=60, performance_score=75, specs={"capacity": "500GB", "type": "NVMe"}, category="storage"),
            
            # Motherboards
            Component(name="B550 ATX", price=120, performance_score=75, specs={"socket": "AM4", "form_factor": "ATX"}, category="motherboard"),
            Component(name="X570 ATX", price=200, performance_score=85, specs={"socket": "AM4", "form_factor": "ATX"}, category="motherboard"),
            Component(name="B660 ATX", price=130, performance_score=78, specs={"socket": "LGA1700", "form_factor": "ATX"}, category="motherboard"),
            
            # Power Supplies
            Component(name="650W 80+ Gold", price=80, performance_score=80, specs={"wattage": "650W", "efficiency": "80+ Gold"}, category="power_supply"),
            Component(name="750W 80+ Gold", price=100, performance_score=85, specs={"wattage": "750W", "efficiency": "80+ Gold"}, category="power_supply"),
            
            # Cases
            Component(name="Mid Tower ATX", price=60, performance_score=70, specs={"form_factor": "ATX", "type": "Mid Tower"}, category="case"),
            Component(name="Full Tower ATX", price=100, performance_score=80, specs={"form_factor": "ATX", "type": "Full Tower"}, category="case"),
        ]
    
    def get_components_by_category(self, category: str) -> List[Component]:
        return [c for c in self.components if c.category == category]
    
    def get_best_component_in_budget(self, category: str, max_price: float) -> Component:
        candidates = [c for c in self.components if c.category == category and c.price <= max_price]
        if not candidates:
            return self.get_components_by_category(category)[0]  # Fallback to cheapest
        return max(candidates, key=lambda c: c.performance_score)