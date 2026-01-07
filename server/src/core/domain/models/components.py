from pydantic import BaseModel
from typing import Dict, Any

class Component(BaseModel):
    name: str
    price: float
    score: int  # 1-100

class ComponentCategory(BaseModel):
    average_price: float

class Cpu(Component):
    ddr: int
    socket: str
    apu_score: int = None

class Gpu(Component):
    vram: int
    frequency: int


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
                self.motherboard.averagePrice + 
                self.ram.averagePrice)