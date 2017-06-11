package main

import (
	"fmt"
)

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

var (
	records = make([]bool, 31)
	length  = 0
)

func SolutionRecursion(A []int, start int) int {
	if start >= length {
		return 0
	}

	startDate := A[start]

	minimum := 0
	for i := start; i < length; i++ {
		if records[A[i]] {
			minimum += 2
		}
	}

	for i := start; i < length; i++ {
		value := A[i]

		if value < 0 {
			continue
		}

		first := value - 6
		if first < start {
			first = start
		}
		current := 0
		for k := value; k >= first; k-- {
			if records[k] {
				current += 1
			}
		}
		if current >= 4 {
			singles := 0
			for j := startDate; j < first; j++ {
				if records[j] {
					singles += 1
				}
			}
			current := singles*2 + 7 + SolutionRecursion(A, i+1)
			if minimum > current {
				minimum = current
			}
		}
	}

	return minimum

}

func Solution(A []int) int {
	// write your code in Go 1.4
	records = make([]bool, 31)
	length = len(A)

	for _, value := range A {
		records[value] = true
	}
	result := SolutionRecursion(A, 0)
	if result > 25 {
		return 25
	}
	return result
}

func main() {
	//fmt.Println(Solution([]int{1, 2, 3, 4, 16, 17, 18, 19, 21}))
	fmt.Println(Solution([]int{1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16}))
	fmt.Println(Solution([]int{1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16, 29, 30}))
	fmt.Println(Solution([]int{1, 2, 5, 6, 7, 9, 10, 11, 14, 15}))
	fmt.Println(Solution([]int{1, 5, 6, 7, 8, 9, 10, 11, 30}))
	fmt.Println(Solution([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30}))
	fmt.Println(Solution([]int{1, 3, 5, 7, 8, 9}))
	fmt.Println(Solution([]int{1}))
	fmt.Println(Solution([]int{1, 3, 5, 7, 8, 10, 12, 14}))
	fmt.Println(Solution([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}))
}
