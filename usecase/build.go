package usecase

import "dreampc/domain"

type build struct {
	coreRepo domain.CoreRepository
}

func NewBuild(coreRepo domain.CoreRepository) domain.BuildUsecase {
	return &build{
		coreRepo: coreRepo,
	}
}

func (b *build) BestByBudgetAndFilters(budget float64, goal domain.BuildGoal) (domain.Build, error) {
	minCoreBudget, err := b.coreRepo.MinimumBudget()
	if err != nil {
		return domain.Build{}, err
	}

	if budget < minCoreBudget {
		return domain.Build{}, domain.ErrInsufficientBudget
	}

	return domain.Build{Price: 1200.00}, nil
}
