package usecase

import "dreampc/domain"

type Build struct{}

func NewBuild() *Build {
	return &Build{}
}

func (b *Build) BestByBudgetAndFilters(budget float64, goal domain.BuildGoal) (domain.Build, error) {
	if budget < 1000 {
		return domain.Build{}, domain.ErrInsufficientBudget
	}

	return domain.Build{Price: 1200.00}, nil
}
