from core.domain.models.components import *
from core.domain.models.machine_config import MachineConfig
from core.domain.models.machine_focus import MachineFocus
from core.usecase.generate_config import GenerateConfigUseCase


def test_generate_config():
    sut = GenerateConfigUseCase()
    result = sut.execute(5000, MachineFocus.COMPETITIVE_GAMING)
    
    socket = "AM4"
    cpu = Cpu(name="good ddr4 cpu", ddr=4, score=1200,socket=socket, hasGraphics=False, price=1500)
    mobo = MotherboardCategory(ddr=4, socket=socket, name="good ddr4 mobo",averagePrice=500)
    ram = RamCategory(ddr=4, frequency=3200, gbCapacity=16, name="8gb ddr4", averagePrice=200)
    gpu = Gpu(name="good gpu", score=1200, price=1500, vram=8, frequency=1800) 

    assert result.total_cost() < 5000
