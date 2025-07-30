package usecase

import (
	"context"
	"dreampc/domain"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCoreUsecase(t *testing.T) {
	coreUsecase := NewCoreUsecase()

	// Test MinBudget
	minBudget, err := coreUsecase.MinBudget(context.Background())
	assert.NoError(t, err)

	assert.Equal(t, domain.Money{Amount: 150000, Currency: domain.CurrencyBRL}, minBudget)
}
