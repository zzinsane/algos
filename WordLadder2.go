package main

/*
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
	    ["hit","hot","dot","dog","cog"],
			    ["hit","hot","lot","log","cog"]
					  ]

*/

import (
	"fmt"
)

type Stack struct {
	Parent  *Stack
	Current int
}

func ifOneStepAway(word1 string, word2 string) bool {
	length := len(word1)
	steps := 0
	for i := 0; i < length; i++ {
		if word1[i] == word2[i] {
			continue
		} else {
			steps++
		}
		if steps > 1 {
			break
		}
	}
	return steps == 1
}

type Queue struct {
	Array []*Stack
	Top   int
}

func (queue *Queue) Enqueue(ele *Stack) {
	if queue.Top == len(queue.Array) {
		newArr := make([]*Stack, len(queue.Array)*2)
		for idx, stack := range queue.Array {
			newArr[idx] = stack
		}
		queue.Array = newArr
	}
	queue.Array[queue.Top] = ele
	queue.Top++
}

func (queue *Queue) Clear() {
	queue.Top = 0
}

func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	if beginWord == endWord {
		return [][]string{}
	}
	diagram := make(map[int][]int)
	result := make([][]string, 0)

	for idx, word := range wordList {
		array, ok := diagram[idx]
		if !ok {
			array = make([]int, 0)
		}
		for idx2, word2 := range wordList {
			if ifOneStepAway(word, word2) {
				array = append(array, idx2)
			}
		}
		diagram[idx] = array
	}
	endIdx := -1
	for idx, word := range wordList {
		if endWord == word {
			endIdx = idx
			break
		}
	}
	if endIdx < 0 {
		return [][]string{}
	}

	queue := &Queue{Array: make([]*Stack, len(wordList)), Top: 0}
	cacheQueue := &Queue{Array: make([]*Stack, len(wordList)), Top: 0}

	visited := make(map[int]int)
	for idx, word := range wordList {
		if ifOneStepAway(beginWord, word) {
			//if idx == endIdx {
			//	return [][]string{[]string{endWord}}
			//}
			queue.Enqueue(&Stack{Parent: nil, Current: idx})
			visited[idx] = 1
		}
	}

	steps := 0
	for {
		steps++
		currentLen := queue.Top
		if currentLen == 0 {
			break
		}

		stop := false
		cacheQueue.Clear()
		for i := 0; i < currentLen; i++ {
			stack := queue.Array[i]
			visited[stack.Current] = 1
			cacheQueue.Enqueue(stack)
		}
		queue.Clear()

		for i := 0; i < currentLen; i++ {
			stack := cacheQueue.Array[i]
			if stack.Current == endIdx {
				stop = true
				oneRe := make([]string, steps+1)
				start := stack
				oneRe[0] = beginWord
				for i := steps; i > 0; i-- {
					oneRe[i] = wordList[start.Current]
					start = start.Parent
				}
				result = append(result, oneRe)
			}

			if stop {
				continue
			}

			if array, ok := diagram[stack.Current]; ok {
				for _, idx := range array {
					if _, idxVisited := visited[idx]; !idxVisited {
						queue.Enqueue(&Stack{Parent: stack, Current: idx})
					}
				}
			}
		}
	}
	return result
}

func main() {
	fmt.Println(findLadders("hit", "cog", []string{"hot", "dot", "lot", "cog"}))
	fmt.Println(findLadders("hit", "cog", []string{"hot", "dot", "dog", "lot", "log", "cog"}))
	//fmt.Println(findLadders("hit", "hot", []string{"hot","dot","dog","lot","log","cog"}))
	//fmt.Println(findLadders("hit", "hit", []string{"hot","dot","dog","lot","log","cog"}))
	fmt.Println(findLadders("qa", "sq", []string{"si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"}))
}
