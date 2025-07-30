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

func (m Money) IsZero() bool {
	return m.Amount == 0
}

func (m Money) LowerThan(other Money) bool {
	if m.Currency != other.Currency {
		return false // or handle currency conversion if needed
	}
	return m.Amount < other.Amount
}

func (m Money) GreaterThan(other Money) bool {
	if m.Currency != other.Currency {
		return false // or handle currency conversion if needed
	}
	return m.Amount > other.Amount
}
