package domain

type Build struct {
	Price float64
}

type BuildUsecase interface {
	BestByBudgetAndFilters(budget float64, goal BuildGoal) (Build, error)
}
