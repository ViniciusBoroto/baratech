package usecase

import (
	"dreampc/internal/domain"
	"dreampc/internal/mocks"
	"testing"

	"github.com/golang/mock/gomock"
	"github.com/stretchr/testify/assert"
)

func TestCoreUsecase_FindBestCore(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()
	type testMocks struct {
		CpuRepo *mocks.MockCpuRepository
	}

	tt := []struct {
		name          string
		budget        float64
		setMocks      func(m *testMocks)
		expectedCore  domain.Core
		expectedError error
	}{
		{
			name:   "Sufficient budget and best build",
			budget: 1000,
			setMocks: func(m *testMocks) {
				m.CpuRepo.EXPECT().AllOrderByScoreDesc().Return([]domain.Cpu{
					{Cores: 6, Speed: 4.0, Socket: "LGA1200", Score: 1500, Price: 300.00},
					{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 1000, Price: 200.00},
					{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 800, Price: 250.00},
				}, nil).Times(1)
			},
			expectedCore: domain.Core{
				Cpu:  domain.Cpu{Cores: 6, Speed: 4.0, Socket: "LGA1200", Score: 1500, Price: 300.00},
				Mobo: domain.Mobo{Socket: "LGA1200", Price: 300.00},
			},
			expectedError: nil,
		},
		{
			name:   "Sufficient budget and second best build",
			budget: 600,
			setMocks: func(m *testMocks) {
				m.CpuRepo.EXPECT().AllOrderByScoreDesc().Return([]domain.Cpu{
					{Cores: 6, Speed: 4.2, Socket: "LGA1200", Score: 2000, Price: 400.00},
					{Cores: 6, Speed: 4.0, Socket: "LGA1200", Score: 1500, Price: 300.00},
					{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 1000, Price: 200.00},
					{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 800, Price: 250.00},
				}, nil).Times(1)
			},
			expectedCore: domain.Core{
				Cpu:  domain.Cpu{Cores: 6, Speed: 4.0, Socket: "LGA1200", Score: 1500, Price: 300.00},
				Mobo: domain.Mobo{Socket: "LGA1200", Price: 300.00},
			},
			expectedError: nil,
		},
		{
			name:   "Insufficient budget for mobo",
			budget: 200,
			setMocks: func(m *testMocks) {
				m.CpuRepo.EXPECT().AllOrderByScoreDesc().Return([]domain.Cpu{
					{Cores: 6, Speed: 4.0, Socket: "LGA1200", Score: 1500, Price: 300.00},
					{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 1000, Price: 200.00},
					{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 800, Price: 250.00},
				}, nil).Times(1)
			},
			expectedCore:  domain.Core{},
			expectedError: domain.ErrInsufficientBudget,
		},
		{
			name:   "Insufficient budget for cpu",
			budget: 100,
			setMocks: func(m *testMocks) {
				m.CpuRepo.EXPECT().AllOrderByScoreDesc().Return([]domain.Cpu{
					{Cores: 6, Speed: 4.0, Socket: "LGA1200", Score: 1500, Price: 300.00},
					{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 1000, Price: 200.00},
					{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 800, Price: 250.00},
				}, nil).Times(1)
			},
			expectedCore:  domain.Core{},
			expectedError: domain.ErrInsufficientBudget,
		},
	}
	for _, tc := range tt {
		t.Run(tc.name, func(t *testing.T) {
			cpuRepo := mocks.NewMockCpuRepository(ctrl)
			usecase := NewCoreUsecase(cpuRepo)
			tc.setMocks(&testMocks{CpuRepo: cpuRepo})

			result, err := usecase.FindBestCore(tc.budget)
			assert.Equal(t, tc.expectedError, err)
			assert.Equal(t, tc.expectedCore, result)
		})
	}
}

func TestCoreUsecase_FindBestCore_WhenInsufficientBudget(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()
	cpuRepo := mocks.NewMockCpuRepository(ctrl)
	usecase := NewCoreUsecase(cpuRepo)

	cpuRepo.EXPECT().AllOrderByScoreDesc().Return([]domain.Cpu{
		{Cores: 6, Speed: 4.0, Socket: "LGA1200", Score: 1500, Price: 300.00},
		{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 1000, Price: 200.00},
		{Cores: 4, Speed: 3.5, Socket: "AM4", Score: 800, Price: 250.00},
	}, nil).Times(1)

	result, err := usecase.FindBestCore(1000)
	assert.NoError(t, err)

	expected := domain.Core{
		Cpu:  domain.Cpu{Cores: 6, Speed: 4.0, Socket: "LGA1200", Score: 1500, Price: 300.00},
		Mobo: domain.Mobo{Socket: "LGA1200", Price: 300.00},
	}
	assert.Equal(t, expected, result)
}
