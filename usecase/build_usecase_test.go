package usecase

// import (
// 	"dreampc/domain"
// 	"dreampc/internal/mocks"
// 	"testing"

// 	"github.com/stretchr/testify/assert"
// )

// func TestBuildUsecase_WhenBudgetLowerThanMinimum(t *testing.T) {
// 	coreRepo := new(mocks.CoreRepository)
// 	sut := NewBuildUsecase(coreRepo)

// 	coreRepo.On("MinBudget").Return(domain.Money{Amount: 30000, Currency: domain.CurrencyBRL}, nil)

// 	_, err := sut.BestByBudget(domain.Money{Amount: 40000, Currency: domain.CurrencyBRL})

// 	assert.Equal(t, domain.ErrNoBuildFound, err)
// }

// func TestBuildUsecase_MinBudget(t *testing.T) {
// 	sut := NewBuildUsecase()

// 	minBudget := domain.Money{Amount: 30000, Currency: domain.CurrencyBRL}

// 	budget := domain.Money{Amount: 40000, Currency: domain.CurrencyBRL}
// 	build, err := sut.BestByBudget(budget)

// 	assert.NoError(t, err)
// 	assert.Equal(t, minBudget.Amount, build.Core.Cpu.Price.Amount)
// 	assert.Equal(t, minBudget.Currency, build.Core.Cpu.Price.Currency)
// }
