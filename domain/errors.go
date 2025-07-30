package domain

import "errors"

var (
	ErrNoBuildFound = errors.New("no build found within the budget")
	ErrNoCpuFound   = errors.New("no CPU found within the budget")
)
