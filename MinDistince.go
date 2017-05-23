package main

import (
	"fmt"
	"math"
)

var (
	word1IdxMapping = make(map[int][]int)
	cache = make(map[string]int)
)


func minDistinceWrapper(word1, word2 string, start1, start2, end1, end2 int) int {

	if v, ok:= cache[fmt.Sprintf("%d_%d-%d_%d", start1, end1, start2, end2)];ok {
		return v
	}

	current := int(math.Max(float64(end1 - start1), float64(end2 - start2)))

	if start1 >= end1 || start2 >= end2 {
		return current
	}

	for idx, _ := range word1[start1:end1] {
		idxArray := word1IdxMapping[idx]
		for _, word2Idx := range idxArray {
			if word2Idx >= start2 && word2Idx < end2{

				v1 := minDistinceWrapper(word1, word2, start1, start2, idx, word2Idx)
				v2 := minDistinceWrapper(word1, word2, idx + 1, word2Idx + 1, end1, end2)


				if (v1+v2) < current {

					//fmt.Println(idx, word2Idx, v1, v2)

					current = v1 + v2
				}
			}
		}
	}

	cache[fmt.Sprintf("%d_%d-%d_%d", start1, end1, start2, end2)] = current

	return current
}

func minDistance(word1 string, word2 string) (result int) {
	// build index mapping

	word1IdxMapping = make(map[int][]int)
	cache = make(map[string]int)

	for idx1, c1 := range word1 {
		idxArray := make([]int, 0)
		for idx2, c2 := range word2 {
			if c1 == c2 {
				idxArray = append(idxArray, idx2)
			}
		}
		word1IdxMapping[idx1] = idxArray
	}

	return minDistinceWrapper(word1, word2, 0, 0, len(word1), len(word2))

}

func main() {
	//fmt.Println(minDistance("aswqfer", "dewrec"))
	//fmt.Println(minDistance("jdewkfnd32324jswqdnqirqrh", "csdnfiewhr232e23i94jwsjdidnd"))

	fmt.Println(minDistance(
		"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef",
		"bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"))

	fmt.Println(minDistance("a", "b"))
}
