package domain

type Build struct {
	Core Core
}

type BuildUsecase interface {
	BestByBudget(budget Money) (Build, error)
}
