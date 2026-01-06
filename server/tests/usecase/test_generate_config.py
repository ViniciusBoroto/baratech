from core.domain.components import *
from core.domain.machine_config import MachineConfig
from core.domain.machine_focus import MachineFocus
from core.usecase.generate_config import GenerateConfigUseCase


def test_generate_config():
    sut = GenerateConfigUseCase()
    sut.execute(5000, MachineFocus.COMPETITIVE_GAMING)
    cpu = Cpu(name="good ddr4 cpu", ddr=4, score=1200,socket="1", hasGraphics=False, price=1500)
    mobo = Motherboard(ddr=4, socket="1", name="good ddr4 mobo", price=500, score=300)
    gpu = Gpu(name="good gpu", score=1200, price=1500)
    ram = Ram(name="8gb ddr4", ddr=4, frequency=3200, price=300, gbCapacity=8, score=8*3200)
    machineConfig = MachineConfig(cpu=cpu, motherboard=mobo, gpu=gpu, ram=[ram], storage=[], powerSupply=None, case=None)   