package usecase

import (
	"dreampc/internal/domain"
	"errors"
)

type core struct {
	cpuRepo domain.CpuRepository
}

func NewCoreUsecase(cpuRepo domain.CpuRepository) domain.CoreUsecase {
	return &core{
		cpuRepo: cpuRepo,
	}
}

func (c *core) FindBestCore(budget float64) (domain.Core, error) {
	cpus, err := c.cpuRepo.AllOrderByScoreDesc()
	if err != nil {
		return domain.Core{}, err
	}
	if len(cpus) == 0 {
		return domain.Core{}, errors.New("no CPUs available")
	}

	var cpu domain.Cpu
	var mobo domain.Mobo
	for {
		var i int
		var err error
		cpu, i, err = c.findBestCpu(cpus, budget)
		if err != nil {
			return domain.Core{}, err
		}

		//TODO: get compatible mobo
		mobo = domain.Mobo{Socket: cpu.Socket, Price: 300.00}

		if cpu.Price+mobo.Price > budget {
			cpus = cpus[i+1:] // Remove the current CPU from the list
			continue          // Try the leftover CPUs
		}
		break
	}
	core := domain.Core{
		Cpu:  cpu,
		Mobo: mobo,
	}

	return core, nil
}

func (c *core) findBestCpu(cpus []domain.Cpu, budget float64) (cpu domain.Cpu, i int, err error) {
	for i, cpu := range cpus {
		if cpu.Price <= budget {
			return cpu, i, nil
		}
	}
	return domain.Cpu{}, 0, domain.ErrInsufficientBudget
}
