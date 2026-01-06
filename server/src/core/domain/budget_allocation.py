from server.src.core.domain.machine_focus import MachineFocus
from typing import Dict

class BudgetAllocationStrategy:
    # Budget allocation weights for each component by focus
    FOCUS_WEIGHTS = {
        MachineFocus.COMPETITIVE_GAMING: {
            'cpu': 0.25,
            'gpu': 0.40,
            'ram': 0.15,
            'storage': 0.08,
            'motherboard': 0.07,
            'power_supply': 0.03,
            'case': 0.02
        },
        MachineFocus.STORY_GAMING: {
            'cpu': 0.20,
            'gpu': 0.45,
            'ram': 0.15,
            'storage': 0.10,
            'motherboard': 0.05,
            'power_supply': 0.03,
            'case': 0.02
        },
        MachineFocus.WORK: {
            'cpu': 0.35,
            'gpu': 0.10,
            'ram': 0.25,
            'storage': 0.15,
            'motherboard': 0.10,
            'power_supply': 0.03,
            'case': 0.02
        },
        MachineFocus.STUDY: {
            'cpu': 0.30,
            'gpu': 0.05,
            'ram': 0.20,
            'storage': 0.25,
            'motherboard': 0.15,
            'power_supply': 0.03,
            'case': 0.02
        },
        MachineFocus.VIDEO_EDITING: {
            'cpu': 0.30,
            'gpu': 0.25,
            'ram': 0.20,
            'storage': 0.15,
            'motherboard': 0.05,
            'power_supply': 0.03,
            'case': 0.02
        }
    }
    
    @classmethod
    def get_allocation(cls, focus: MachineFocus, budget: float) -> Dict[str, float]:
        weights = cls.FOCUS_WEIGHTS[focus]
        return {component: budget * weight for component, weight in weights.items()}