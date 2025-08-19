package usecase

// type build struct {
// 	core domain.CoreUsecase
// }

// func NewBuild(core domain.CoreUsecase) domain.BuildUsecase {
// 	return &build{
// 		core: core,
// 	}
// }

// func (b *build) BestByBudgetAndFilters(budget float64, goal domain.BuildGoal) (domain.Build, error) {
// 	minCoreBudget, err := b.core.MinimumBudget()
// 	if err != nil {
// 		return domain.Build{}, err
// 	}

// 	if budget < minCoreBudget {
// 		return domain.Build{}, domain.ErrInsufficientBudget
// 	}

// 	return domain.Build{Price: 1200.00}, nil
// }
