package domain

import "context"

type Core struct {
	Cpu    Cpu
	Mobo   Mobo
	Rams   []Ram
	Cooler CpuCooler
}

type CoreUsecase interface {
	MinBudget(ctx context.Context) (Money, error)
}
