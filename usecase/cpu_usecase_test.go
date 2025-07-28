package usecase

import (
	"dreampc/domain"
	"dreampc/internal/mocks"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestBestByBudget(t *testing.T) {
	cpu := domain.Cpu{
		Brand:      domain.CpuBrandAMD,
		Price:      domain.Money{Amount: 75000, Currency: domain.CurrencyBRL},
		Model:      "Ryzen 5",
		Generation: "5600",
	}
	cpus := []domain.Cpu{
		cpu,
		{
			Brand:      domain.CpuBrandIntel,
			Price:      domain.Money{Amount: 65000, Currency: domain.CurrencyBRL},
			Model:      "Core i5",
			Generation: "11400",
			Score:      domain.CpuScore{Multitask: 12000, Gaming: 1500},
		},
	}
	cpuRepo := new(mocks.CpuRepository)

	budget := domain.Money{
		Amount:   80000,
		Currency: domain.CurrencyBRL,
	}
	cpuRepo.On("All").Return(cpus, nil)
	sut := NewCpuUsecase(cpuRepo)

	res, err := sut.BestByBudget(budget)
	assert.NoError(t, err)

	assert.Equal(t, cpu.Model, res.Model)
	assert.Equal(t, cpu.Generation, res.Generation)
}
