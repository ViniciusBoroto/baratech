import pytest
from unittest.mock import Mock
from core.domain.models.components import *
from core.domain.models.machine_config import MachineConfig
from core.domain.models.machine_focus import MachineFocus
from core.usecase.generate_config import GenerateConfigUseCase


def test_generate_config_total_cost_lower_than_budget():
    # Create mock repositories
    cpu_repo_mock = Mock()
    mobo_repo_mock = Mock()
    ram_repo_mock = Mock()
    
    # Create test data
    affordable_cpu = Cpu(name="Test CPU", price=1000, score=85, ddr=4, socket="AM4")
    expensive_cpu = Cpu(name="Expensive CPU", price=6000, score=95, ddr=4, socket="AM4")
    test_mobo = MotherboardCategory(average_price=200, socket="AM4", ddr=4)
    test_ram = RamCategory(average_price=150, ddr=4, frequency=3200, gb_capacity=16)
    
    # Configure mock return values
    cpu_repo_mock.get_all_by_budget.return_value = [expensive_cpu, affordable_cpu]
    mobo_repo_mock.get_all_by_budget.return_value = [test_mobo]
    ram_repo_mock.get_all_by_budget.return_value = [test_ram]
    
    sut = GenerateConfigUseCase(cpu_repo_mock, mobo_repo_mock, ram_repo_mock)
    budget = 5000
    result = sut.execute(budget, MachineFocus.COMPETITIVE_GAMING)
    
    # Verify mocks were called with correct budget
    cpu_repo_mock.get_all_by_budget.assert_called_once_with(budget)
    mobo_repo_mock.get_all_by_budget.assert_called_once_with(budget)
    ram_repo_mock.get_all_by_budget.assert_called_once_with(budget)
    
    assert isinstance(result, MachineConfig)
    assert result.processingKit.cpu == affordable_cpu
    assert result.processingKit.motherboard == test_mobo
    assert result.processingKit.ram == test_ram

def test_generate_config_get_best_performance_on_budget():
    # Create mock repositories
    cpu_repo_mock = Mock()
    mobo_repo_mock = Mock()
    ram_repo_mock = Mock()
    
    # Create test data
    affordable_weak_cpu = Cpu(name="Test weak CPU", price=1000, score=85, ddr=4, socket="AM4")
    affordable_strong_cpu = Cpu(name="Test strong CPU", price=1000, score=92, ddr=4, socket="AM4")
    expensive_cpu = Cpu(name="Expensive CPU", price=6000, score=95, ddr=4, socket="AM4")
    test_mobo = MotherboardCategory(average_price=200, socket="AM4", ddr=4)
    test_ram = RamCategory(average_price=150, ddr=4, frequency=3200, gb_capacity=16)
    
    # Configure mock return values
    cpu_repo_mock.get_all_by_budget.return_value = [expensive_cpu, affordable_weak_cpu,  affordable_strong_cpu]
    mobo_repo_mock.get_all_by_budget.return_value = [test_mobo]
    ram_repo_mock.get_all_by_budget.return_value = [test_ram]
    
    sut = GenerateConfigUseCase(cpu_repo_mock, mobo_repo_mock, ram_repo_mock)
    budget = 5000
    
    result = sut.execute(budget, MachineFocus.COMPETITIVE_GAMING)
    
    # Verify mocks were called with correct budget
    cpu_repo_mock.get_all_by_budget.assert_called_once_with(budget)
    mobo_repo_mock.get_all_by_budget.assert_called_once_with(budget)
    ram_repo_mock.get_all_by_budget.assert_called_once_with(budget)
    
    assert isinstance(result, MachineConfig)
    assert result.processingKit.cpu == affordable_strong_cpu
    assert result.processingKit.motherboard == test_mobo
    assert result.processingKit.ram == test_ram

