package service

import (
	"dreampc/internal/domain"
	"dreampc/internal/mocks"
	"testing"

	"github.com/golang/mock/gomock"
	"github.com/stretchr/testify/assert"
)

func TestMoboService(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()

	moboRepo := mocks.NewMockMoboRepository(ctrl)

	cpu := domain.Cpu{
		Socket: "LGA1200",
	}
	moboRepo.EXPECT().FindBySocketOrderByPrice(cpu.Socket)

	sut := NewMobo(moboRepo)
	res, err := sut.FindCheaperCompatible(cpu)
	assert.NoError(t, err)

	assert.Equal(t, cpu.Socket, res.Socket)
}
