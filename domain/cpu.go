package domain

type Cpu struct {
	Cores  int
	Speed  float64
	Socket string
	Score  float64
	Price  float64
}

type CpuRepository interface {
	AllOrderByScoreDesc() ([]Cpu, error)
}
