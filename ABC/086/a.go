package main

import (
	"fmt"
)

func main() {
	var a, b int

	fmt.Scan(&a, &b)
	product := a * b

	if isEven(product) {
		fmt.Println("Even")
	} else {
		fmt.Println("Odd")
	}
}

func isEven(num int) bool {
	if num % 2 == 0 {
		return true
	}
	return false
}