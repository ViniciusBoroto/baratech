package domain

import "context"

type CpuBrand string

const (
	CpuBrandAMD   CpuBrand = "AMD"
	CpuBrandIntel CpuBrand = "Intel"
)

type CpuScore struct {
	Multitask int
	Gaming    int
}

func (c CpuScore) Total() int {
	return c.Multitask + c.Gaming
}

type Cpu struct {
	Brand      CpuBrand
	Score      CpuScore
	Price      Money
	Model      string
	Generation string
	Socket     string
}

type CpuCooler struct {
	TDP    int
	Socket string
}

type CpuRepository interface {
	All(ctx context.Context) ([]Cpu, error)
	Cheapest(ctx context.Context) (Cpu, error)
}

type CpuUsecase interface {
	BestByBudget(budget Money) (Cpu, error)
}
