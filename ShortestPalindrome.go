package main

/*
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

this one is easy, just find longest parlindrome string starting from first char
*/

import "fmt"

func longestPlindrome(s string) int {
	length := len(s)
	matchedLen := 1
	for i := 1; i < length; i++ {
		half := i / 2

		matched := true
		for k := 0; k < half+1; k++ {
			mirror := i - k
			if s[k] != s[mirror] {
				matched = false
				break
			}
		}
		if matched {
			matchedLen = i + 1
		}
	}
	return matchedLen
}

func shortestPalindrome(s string) string {
	length := len(s)
	if length == 0 {
		return ""
	}
	extendLen := length - longestPlindrome(s)
	extend := make([]byte, extendLen)
	for i := 0; i < extendLen; i++ {
		extend[i] = s[length-i-1]
	}
	return string(extend) + s
}

func main() {

	fmt.Println(shortestPalindrome("aaaaaaaab"))
	fmt.Println(shortestPalindrome("aaaaaababds"))
	fmt.Println(shortestPalindrome(""))
}
