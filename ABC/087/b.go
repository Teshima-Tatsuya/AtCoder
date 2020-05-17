package main

import (
	"fmt"
)

func main() {
	var A, B, C, N int
	fmt.Scan(&A, &B, &C, &N)

	fmt.Println(coins(A, B, C, N))
}

func coins(A, B, C, N int) int {
	result := 0
	for i := 0; i <= A; i++ {
		for j := 0; j <= B; j++ {
			for k := 0; k <= C; k++ {
				sum := i * 500 + j* 100 + k*50
				if N == sum {
					result++
				}
			}
		}
	}

	return result
}