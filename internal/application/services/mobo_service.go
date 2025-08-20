package service

import (
	"dreampc/internal/domain"
	"errors"
)

type MoboService interface {
	FindCheaperCompatible(cpu domain.Cpu) (domain.Mobo, error)
}

type moboService struct {
	moboRepo domain.MoboRepository
}

func NewMobo(moboRepo domain.MoboRepository) MoboService {
	return &moboService{
		moboRepo: moboRepo,
	}
}

func (m *moboService) FindCheaperCompatible(cpu domain.Cpu) (domain.Mobo, error) {
	mobos, err := m.moboRepo.FindBySocketOrderByPrice(cpu.Socket)
	if err != nil {
		return domain.Mobo{}, err
	}
	if len(mobos) == 0 {
		return domain.Mobo{}, errors.New("no mobos found for socket")
	}

	return mobos[0], nil
}
