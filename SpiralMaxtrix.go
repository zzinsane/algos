package main

import "fmt"

/*
key idea is to four types of walkings,
0: →
1: ↓
2: ←
3: ↑
and update boundaries after each walking
*/

func spiralMatrix(matrix [][]int) {
	length := len(matrix[0])
	lowerIdx := []int{0, 0}
	upperIdx := []int{length - 1, length - 1}

	//startX := 0
	//startY := 0

	iterateType := 0

	result := make([]int, 0)
	for {
		if lowerIdx[0] > upperIdx[0] && lowerIdx[1] > upperIdx[1] {
			break
		}

		var newLine []int
		if iterateType == 0 {
			newLine = matrix[lowerIdx[0]][lowerIdx[1] : upperIdx[1]+1]
			lowerIdx[0] += 1

		} else if iterateType == 1 {
			newLine = make([]int, 0)

			for i := lowerIdx[0]; i <= upperIdx[0]; i++ {

				newLine = append(newLine, matrix[i][upperIdx[1]])
			}
			upperIdx[1] -= 1
		} else if iterateType == 2 {
			newLine = make([]int, 0)
			for i := upperIdx[1]; i >= lowerIdx[1]; i-- {
				newLine = append(newLine, matrix[upperIdx[0]][i])
			}
			upperIdx[0] -= 1
		} else {
			newLine = make([]int, 0)
			for i := upperIdx[0]; i >= lowerIdx[0]; i-- {
				newLine = append(newLine, matrix[i][lowerIdx[1]])
			}
			lowerIdx[1] += 1
		}
		for _, v := range newLine {
			result = append(result, v)
		}

		iterateType += 1
		iterateType = iterateType % 4

	}
	fmt.Println(result)

}

func main() {
	matrix := [][]int{
		[]int{1, 2, 3, 4},
		[]int{5, 6, 7, 8},
		[]int{9, 10, 11, 12},
		[]int{13, 14, 15, 16},
	}
	spiralMatrix(matrix)
}
