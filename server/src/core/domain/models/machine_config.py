from pydantic import BaseModel

from core.domain.models import *
from typing import List

from core.domain.models.components import *

class MachineConfig(BaseModel):
    processingKit: ProcessingKit
    gpu: Gpu

    def socket(self) -> str:
        return self.processingKit.cpu.socket
    def total_cost(self) -> float:
        return (self.processingKit.average_price() + 
                self.gpu.price)