package usecase

import (
	"context"
	"dreampc/domain"
)

type coreUsecase struct {
	cpuRepo domain.CpuRepository
}

func NewCoreUsecase(cpuRepo domain.CpuRepository) domain.CoreUsecase {
	return &coreUsecase{cpuRepo: cpuRepo}
}

func (c *coreUsecase) MinBudget(ctx context.Context) (domain.Money, error) {
	cpu, err := c.cpuRepo.Cheapest(ctx)
	if err != nil {
		return domain.Money{}, err
	}

	return domain.Money{Amount: cpu.Price.Amount + 60000, Currency: domain.CurrencyBRL}, nil
}
