package usecase

import "dreampc/domain"

type core struct {
	cpuRepo domain.CpuRepository
}

func NewCoreUsecase(cpuRepo domain.CpuRepository) domain.CoreUsecase {
	return &core{
		cpuRepo: cpuRepo,
	}
}

func (c *core) FindBestCore(budget float64) (domain.Core, error) {
	cpus, _ := c.cpuRepo.AllOrderByScoreDesc()

	core := domain.Core{
		Cpu:  cpus[0],
		Mobo: domain.Mobo{Socket: "LGA1200", Price: 300.00},
	}

	return core, nil
}
