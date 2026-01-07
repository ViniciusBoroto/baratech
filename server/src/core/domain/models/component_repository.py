from abc import ABC, abstractmethod
from typing import List

from core.domain.models import Component

class ComponentRepository(ABC):
    @abstractmethod
    def get_components_by_category(self, category: str) -> List[Component]:
        pass
    
    @abstractmethod
    def get_best_component_in_budget(self, category: str, max_price: float) -> Component:
        pass