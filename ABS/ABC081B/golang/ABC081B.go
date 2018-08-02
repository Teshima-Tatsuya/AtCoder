package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	sc.Split(bufio.ScanWords)
	N := nextInt()
	nums := []int{}
	for i := 0; i < N; i++ {
		nums = append(nums, nextInt())
	}

	flag := true
	result := 0
	for i := 1; ; i++ {
		for j, num := range nums {
			if num%2 == 0 {
				nums[j] = num / 2
			} else {
				flag = false
			}
		}
		if !flag {
			break
		}

		result++
	}

	fmt.Println(result)
}

func nextInt() int {
	sc.Scan()
	i, _ := strconv.Atoi(sc.Text())

	return i
}
