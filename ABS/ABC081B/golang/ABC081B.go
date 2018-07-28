package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	N := nextInt()

	a := []int{}
	for i := 0; i < N; i++ {
		a = append(a, nextInt())
	}

	flag := true
	result := 0
	for i := 1; ; i++ {
		for _, num := range a {
			if num%int(math.Pow(float64(2), float64(i))) != 0 {
				flag = false
				break
			}
		}
		if flag {
			result++
		} else {
			break
		}
	}

	fmt.Println(result)
}

func nextInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}

	return i
}
