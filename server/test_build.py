import sys
sys.path.append('/home/vinicius/Documents/development/baratech2')

from server.src.core.usecase.generate_specs import GenerateSpecsUseCase
from server.src.core.domain.machine_focus import MachineFocus

def test_build_generation():
    use_case = GenerateSpecsUseCase()
    
    # Test different focuses with same budget
    budget = 1500
    
    print(f"Budget: ${budget}")
    print("=" * 50)
    
    for focus in MachineFocus:
        config = use_case.execute(budget, focus.value)
        print(f"\n{focus.value.upper()} BUILD:")
        print(f"CPU: {config.cpu}")
        print(f"GPU: {config.gpu}")
        print(f"RAM: {config.ram}")
        print(f"Storage: {config.storage}")
        print(f"Motherboard: {config.motherboard}")
        print(f"Power Supply: {config.powerSupply}")
        print(f"Case: {config.case}")

if __name__ == "__main__":
    test_build_generation()