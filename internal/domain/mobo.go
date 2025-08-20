package domain

type Mobo struct {
	Socket string
	Price  float64
}

type MoboRepository interface {
	FindBySocketOrderByPrice(socket string) ([]Mobo, error)
}
