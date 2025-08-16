package domain

type CoreRepository interface {
	MinimumBudget() (float64, error)
}
