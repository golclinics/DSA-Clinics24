package gatimugabriel

import (
	"math"
	"testing"
)

func TestReverseInteger(t *testing.T) {
	//  500, -56, -90, 91, 
	testCases := []struct {
		name     string
		input    int
		expected int
	}{
		{
			name:     "case positive number",
			input:    500,
			expected: 5,
		},
		{
			name:     "case negative number",
			input:    -56,
			expected: -65,
		},
		{
			name:     "case negative number 2",
			input:    -90,
			expected: -9,
		},
		{
			name:     "case positive number 2",
			input:    91,
			expected: 19,
		},
		{
			name:     "max int32 overflow",
			input:    math.MaxInt32,
			expected: 0,
		},
		{
			name:     "min int32 overflow",
			input:    math.MinInt32,
			expected: 0,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := Reverse(tc.input)
			if result != tc.expected {
				t.Errorf("Test %s failed: input=%d, got %d, expected=%d", tc.name, tc.input, result, tc.expected)
			}
		})
	}
}
