package main

/*
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
*/

import (
	"fmt"
	"math"
)

var (
	word1IdxMapping = make(map[int][]int)
	cache           = make(map[string]int)
	len1            = 0
	len2            = 0
)

func stretch(word1, word2 string, start1, start2 int, end1, end2 int) int {

	length := 0
	for {
		idx1 := start1 + length
		idx2 := start2 + length

		if idx1 < end1 && idx2 < end2 && word1[idx1] == word2[idx2] {
			length += 1
		} else {
			return length
		}
	}
}

func minDistinceWrapper(word1, word2 string, start1, start2, end1, end2 int) int {

	if v, ok := cache[fmt.Sprintf("%d_%d-%d_%d", start1, end1, start2, end2)]; ok {
		return v
	}

	current := int(math.Max(float64(end1-start1), float64(end2-start2)))

	if start1 >= end1 || start2 >= end2 {

		return current
	}

	for idxI, _ := range word1[start1:end1] {
		idx := idxI + start1
		idxArray := word1IdxMapping[idx]
		for _, word2Idx := range idxArray {

			if word2Idx >= start2 && word2Idx < end2 {
				stretchLen := stretch(word1, word2, idx, word2Idx, end1, end2)

				start21 := idx + stretchLen
				start22 := word2Idx + stretchLen

				minimum := math.Abs(float64((idx-start1)-(word2Idx-start2))) + math.Abs(float64((end1-start21)-(end2-start22)))
				if int(minimum) >= current {
					continue
				}

				v1 := minDistinceWrapper(word1, word2, start1, start2, idx, word2Idx)

				if v1 > current {
					continue
				}

				v2 := minDistinceWrapper(word1, word2, start21, start22, end1, end2)

				if (v1 + v2) < current {

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
	len1 = len(word1)
	len2 = len(word2)

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
	fmt.Println(minDistance("adewd3efqwiedeiquwfoerbfrebfibewofeqr epqwhdewuqh zwewjrew zrfeuturegt", "bjdiewnqfdefefnvfrbgbfebfrefbvfevbfriwugbeife dweidewfhure"))
	fmt.Println(minDistance("teacher", "reteaches"))
}
