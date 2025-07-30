package domain

import "dreampc/domain"

type Mobo struct {
	Brand  string
	Model  string
	Socket string
	DDR    int
}

type MoboUsecase interface {
	CheapestByCpu(cpu domain.Cpu) (Mobo, error)
}

type MoboRepository interface {
	CheapestCompatible(socket string, ddr int, tdp int) ([]Mobo, error)
}
