package usecase

import (
	"dreampc/domain"
)

type cpuUsecase struct {
	cpuRepository domain.CpuRepository
}

func NewCpuUsecase(cpuRepo domain.CpuRepository) domain.CpuUsecase {
	return &cpuUsecase{
		cpuRepository: cpuRepo,
	}
}

func (c *cpuUsecase) BestByBudget(budget domain.Money) (domain.Cpu, error) {
	cpus, err := c.cpuRepository.All()
	if err != nil {
		return domain.Cpu{}, err
	}

	var bestCpu domain.Cpu
	for _, cpu := range cpus {
		if cpu.Price.Amount <= budget.Amount && cpu.Score.Multitask > bestCpu.Score.Multitask {
			bestCpu = cpu
		}
	}
	if bestCpu.Model == "" {
		return domain.Cpu{}, domain.ErrNoCpuFound
	}

	return bestCpu, nil
}
