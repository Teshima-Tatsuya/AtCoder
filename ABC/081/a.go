package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string

	fmt.Scan(&s)

	marblePlaced := strings.Count(s, "1")
	fmt.Println(marblePlaced)

}
