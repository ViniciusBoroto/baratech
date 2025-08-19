package domain

type Core struct {
	Cpu  Cpu
	Mobo Mobo
}

type CoreService interface {
	FindBestCore(budget float64) (Core, error)
}
