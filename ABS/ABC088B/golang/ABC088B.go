package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	a := make([]int, N)

	fmt.Scan(&N)

	for i := 0; i < N; i++ {
		fmt.Scan(&a[i])
		fmt.Println(a[i])
	}

	sort.Ints(a)

	for i := 0; i < N; i++ {
		fmt.Println(a[i])
	}

}
