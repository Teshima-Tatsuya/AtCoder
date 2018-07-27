package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer = bufio.NewWriter(os.Stdout)

func main() {
	var N, Q int
	var ans string

	fmt.Scan(&N, &Q)
	fmt.Fprintln("%d %d", N, Q)
	
	fmt.Fprintln(writer, "? A B")
	_ = writer.Flush()

	fmt.Scan(&ans)
	fmt.Printf("test %s", ans)
}