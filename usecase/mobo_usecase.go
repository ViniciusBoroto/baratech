package usecase

type moboUsecase struct {
	moboRepo domain.MoboRepository
}

func NewMoboUsecase(moboRepo domain.MoboRepository) domain.MoboUsecase {
	return &moboUsecase{moboRepo: moboRepo}
}
