from pydantic import BaseModel
from typing import Dict, Any



class Component(BaseModel):
    name: str
    price: float

class ComponentCategory(BaseModel):
    average_price: float

def _relative_score(score: int, maximum_reference: int):
    return score / maximum_reference * 100

class Cpu(Component):
    ddr: int
    socket: str
    score: int
    apu_score: int | None = None
    def get_relative_score(self, maximum_reference: int):
        return _relative_score(self.score, maximum_reference)
    def get_relative_apu_score(self, maximum_reference: int):
        return _relative_score(self.apu_score, maximum_reference)

class Gpu(Component):
    vram: int
    frequency: int
    score: int
    def get_relative_score(self, maximum_reference: int):
        return _relative_score(self.score, maximum_reference)


#Categories
class MotherboardCategory(ComponentCategory):
    socket: str
    ddr: int
    def accepts_cpu(self, cpu: Cpu) -> bool:
        return cpu.socket == self.socket and cpu.ddr == self.ddr
    def accepts_ram(self, ram: 'RamCategory') -> bool:
        return ram.ddr == self.ddr

class RamCategory(ComponentCategory):
    ddr: int
    frequency: int
    gb_capacity: int

class PowerSupplyCategory(ComponentCategory):
    minimum_wattage: int
    minimum_efficiency: str
 
class StorageCategory(ComponentCategory):
    capacity: int
    type: str

class CaseCategory(ComponentCategory):
    size: str
    type: str


#### Aggregates ####
class ProcessingKit(BaseModel):
    cpu: Cpu
    motherboard: MotherboardCategory
    ram: RamCategory

    def average_price(self) -> float:
        return (self.cpu.price + 
                self.motherboard.average_price + 
                self.ram.average_price)