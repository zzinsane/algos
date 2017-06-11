package main

/*
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

typical dynamic programming problem
*/
import (
	"fmt"
	"strings"
)

type Ele struct {
	Array  []int
	cursor int
	start  int
}

type Stack struct {
	Array []*Ele
	Size  int
	Top   int
}

func (stack *Stack) Push(ele *Ele) {
	stack.Array[stack.Top] = ele
	stack.Top++
}

func (stack *Stack) Pop() *Ele {
	if stack.Top <= 0 {
		return nil
	}
	stack.Top--
	return stack.Array[stack.Top]
}

func (stack *Stack) TOPEle() *Ele {
	if stack.Top <= 0 {
		return nil
	}
	return stack.Array[stack.Top-1]
}

func wordBreakWithStack(s string, wordDict []string) []string {
	length := len(s)
	word1IdxMapping := make(map[int][]int)

	for idx, str := range wordDict {
		currentLen := len(str)
		for i := 0; i < length; i++ {
			matched := true
			for j := 0; j < currentLen; j++ {
				if i+j >= length || s[i+j] != str[j] {
					matched = false
					break
				}
			}
			if matched {
				array, ok := word1IdxMapping[i]
				if !ok {
					array = make([]int, 0)
				}
				array = append(array, idx)
				word1IdxMapping[i] = array
			}
		}
	}

	stack := Stack{
		Array: make([]*Ele, length),
		Top:   0,
		Size:  length,
	}

	start, ok := word1IdxMapping[0]
	if !ok {
		start = make([]int, 0)
	}
	stack.Push(&Ele{
		Array:  start,
		cursor: -1,
		start:  0,
	})
	results := make([]string, 0)

	for {

		ele := stack.TOPEle()
		if ele == nil {
			break
		}

		needPop := true
		for i := ele.cursor + 1; i < len(ele.Array); i++ {
			ele.cursor = i
			next := ele.start + len(wordDict[ele.Array[i]])
			if next == length {
				substrings := make([]string, 0)
				for i := 0; i < stack.Top; i++ {
					ele := stack.Array[i]
					substrings = append(substrings, wordDict[ele.Array[ele.cursor]])
				}
				results = append(results, strings.Join(substrings, " "))

			} else if next < length {
				if nextArray, ok := word1IdxMapping[next]; ok {

					stack.Push(&Ele{
						Array:  nextArray,
						cursor: -1,
						start:  next,
					})
					needPop = false
					break
				} else {
					continue
				}
			} else {
				continue
			}
		}
		if needPop {
			stack.Pop()
		}
	}

	return results
}

var (
	wordMapping map[int][]int
	wordsDict   []string
	ss          string
	length      int
	cache       map[int][]string
)

func wordBreakWithRecursionWrap(start int) []string {
	if words, ok := cache[start]; ok {
		return words
	}

	result := make([]string, 0)
	if idxes, ok := wordMapping[start]; ok {
		for _, idx := range idxes {
			word := wordsDict[idx]
			if start+len(word) == length {
				result = append(result, word)
			} else {
				wordsArray := wordBreakWithRecursionWrap(start + len(word))

				for _, extendWord := range wordsArray {
					result = append(result, word+" "+extendWord)
				}
			}
		}
	}
	cache[start] = result
	return result
}

func wordBreakWithRecursion(s string, wordDict []string) []string {
	length = len(s)
	wordMapping = make(map[int][]int)
	wordsDict = wordDict
	ss = s
	cache = make(map[int][]string)

	for idx, str := range wordDict {
		currentLen := len(str)
		for i := 0; i < length; i++ {
			matched := true
			for j := 0; j < currentLen; j++ {
				if i+j >= length || s[i+j] != str[j] {
					matched = false
					break
				}
			}
			if matched {
				array, ok := wordMapping[i]
				if !ok {
					array = make([]int, 0)
				}
				array = append(array, idx)
				wordMapping[i] = array
			}
		}
	}
	return wordBreakWithRecursionWrap(0)
}

func wordBreak(s string, wordDict []string) []string {
	return wordBreakWithRecursion(s, wordDict)
}

func main() {
	fmt.Println(
		wordBreak(
			"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
			[]string{"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"}))
}
