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
	return domain.Cpu{
		Model:      "Ryzen 5",
		Generation: "5600",
	}, nil
}
