package main

import (
	"fmt"
)

func main() {
	var N, A, B int
	fmt.Scan(&N, &A, &B)

	result := 0
	for i := 1; i <= N; i++ {
		sum := sumDigits(i)

		if A <= sum && sum <= B {
			result += i
		}
	}

	fmt.Println(result)
}

func sumDigits(N int) (sum int) {
	for N != 0 {
		sum += N % 10
		N /= 10
	}

	return
}