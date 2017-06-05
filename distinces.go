package main

import "fmt"

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(T []int) []int {
	// write your code in Go 1.4

	length := len(T)
	idxes := make([][]int, length)
	capital := -1
	for idx, value := range T {
		if idx == value {
			capital = idx
		} else {
			idxes[value] = append(idxes[value], idx)
		}
	}
	queue := make(chan int, length)
	queue <- capital

	result := make([]int, length - 1)
	steps := -1
	for {
		if len(queue) == 0 {
			break
		}
		qlen := len(queue)
		if steps >=0 {
			result[steps] = len(queue)
		}
		for i:=0;i<qlen;i++ {
			city := <- queue
			for _, v := range idxes[city] {
				queue <- v
			}
		}

		steps += 1
	}
	return result
}

func main(){
	fmt.Println(Solution([]int{9, 1, 4, 9, 0, 4, 8, 9, 0, 1}))
}

