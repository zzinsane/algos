package main

import (
	"fmt"
	"strconv"
)

func wrapper(s string) int {
	if len(s) == 0 {
		return 1
	}

	if s[0:1] == "0" {
		return 0
	}

	val, _ := strconv.Atoi(s)

	if len(s) == 1 {
		return 1
	}

	if val == 10 || val == 20 {
		return 1
	}

	if val > 10 && val < 27 {
		return 2
	}

	if val%10 == 0 {
		return 0
	}

	return 1
}

func numDecodings(s string) int {

	if len(s) == 0 {
		return 0
	}
	return numDecodingsWrapper(s)
}

func numDecodingsWrapper(s string) int {

	if len(s) < 3 {
		return wrapper(s)
	}

	first2 := s[0:2]
	variations := wrapper(first2)

	current := variations * numDecodingsWrapper(s[2:])

	seconds2 := s[1:3]
	variations = wrapper(seconds2)
	if (variations == 1 && (seconds2 == "10" || seconds2 == "20")) || variations == 2 {
		current += wrapper(s[0:1]) * numDecodingsWrapper(s[3:])
	}

	return current
}

func main() {
	//fmt.Println(numDecodings("3342353256465"))
	//fmt.Println(numDecodings("12134048398423573758937549369436"))
	//fmt.Println(numDecodings("1213448398573758937549324832048546574865369436"))
	//fmt.Println(numDecodings("1213448398573758937549324832048546574865360343432509436"))
	//fmt.Println(numDecodings(""))
	fmt.Println(numDecodings("110"))
}
