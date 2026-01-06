from pydantic import BaseModel

class MachineConfig(BaseModel):
    cpu: str
    gpu: str
    ram: str
    storage: str
    motherboard: str
    powerSupply: str
    case: str