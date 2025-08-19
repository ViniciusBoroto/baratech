package service

import (
	"dreampc/internal/domain"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMoboService(t *testing.T) {
	sut := NewMobo()
	cpu := domain.Cpu{
		Socket: "LGA1200",
	}
	res, err := sut.FindCheaperCompatible(cpu)
	assert.NoError(t, err)

	assert.Equal(t, cpu.Socket, res.Socket)
}
