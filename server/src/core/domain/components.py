from pydantic import BaseModel
from typing import Dict, Any

class Component(BaseModel):
    name: str
    price: float
    score: int  # 1-100
    category: str  # cpu, gpu, ram, storage, motherboard, power_supply, case

class Cpu(Component):
    ddr: int
    socket: str
    hasGraphics: bool

class Motherboard(Component):
    socket: str
    ddr: int

class Ram(Component):
    ddr: int
    frequency: int

class Gpu(Component):
    vram: int
    frequency: int

class PowerSupply(Component):
    wattage: int
    efficiency: str
 
class Storage(Component):
    capacity: int
    type: str

class Case(Component):
    size: str
    type: str


#### Aggregates ####
class Core(BaseModel):
    cpu: Cpu
    motherboard: Motherboard
    ram: list[Ram]
