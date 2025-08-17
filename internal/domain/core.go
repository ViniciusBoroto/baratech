package domain

type Core struct {
	Cpu  Cpu
	Mobo Mobo
}

type CoreUsecase interface {
	FindBestCore(budget float64) (Core, error)
}
