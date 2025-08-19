package service

import "dreampc/internal/domain"

type MoboService interface {
	FindCheaperCompatible(cpu domain.Cpu) (domain.Mobo, error)
}

type moboService struct {
}

func NewMobo() MoboService {
	return &moboService{}
}

func (m *moboService) FindCheaperCompatible(cpu domain.Cpu) (domain.Mobo, error) {
	return domain.Mobo{Socket: "LGA1200"}, nil
}
