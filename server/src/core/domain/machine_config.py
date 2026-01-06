from pydantic import BaseModel

from core.domain.components import *
from typing import List

class MachineConfig(BaseModel):
    # core: Core
    gpu: Gpu
    storage: List[Storage]
    powerSupply: PowerSupply
    computerCase: Case