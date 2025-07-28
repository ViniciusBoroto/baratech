package domain

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
}

type CpuRepository interface {
	All() ([]Cpu, error)
}

type CpuUsecase interface {
	BestByBudget(budget Money) (Cpu, error)
}
