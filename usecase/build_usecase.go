package usecase

// import "dreampc/domain"

// type buildUsecase struct {
// 	coreRepo domain.CoreUsecase
// }

// func NewBuildUsecase(coreRepo domain.CoreUsecase) domain.BuildUsecase {
// 	return &buildUsecase{coreRepo: coreRepo}
// }

// func (b *buildUsecase) BestByBudget(budget domain.Money) (domain.Build, error) {
// 	minBudget, err := b.coreRepo.MinBudget()
// 	if err != nil {
// 		return domain.Build{}, err
// 	}

// 	if budget.Amount < minBudget.Amount {
// 		return domain.Build{}, domain.ErrNoBuildFound
// 	}

// 	core := domain.Core{} // This would be populated with the best core based on the budget.
// 	return domain.Build{Core: core}, nil
// }
