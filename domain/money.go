package domain

type Currency string

const (
	CurrencyBRL Currency = "BRL"
	CurrencyUSD Currency = "USD"
)

type Money struct {
	Amount   int64
	Currency Currency
}
