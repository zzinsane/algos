package main

import (
	"strings"
)

var (
	separator = "_"
)

func singleLinePadding(words []string, maxWidth int, isLastLine bool) string {
	if isLastLine {
		joined := strings.Join(words, separator)
		joined = joined + strings.Repeat(separator, maxWidth - len(joined))
		return joined
	}

	length := len(words)

	total := 0
	for _, word := range words {
		total += len(word)
	}

	if length == 1 {
		return words[0] + strings.Repeat(separator, maxWidth - total)
	}

	each := (maxWidth - total)/(length - 1)
	surplus := (maxWidth -total)%(length - 1)

	final := ""
	for i:=0;i<surplus;i++ {
		final += words[i]
		final += strings.Repeat(separator, each + 1)
	}
	for i:=surplus;i<length - 1;i++ {
		final += words[i]
		final += strings.Repeat(separator, each)
	}
	final += words[length - 1]
	return final
}

func fullJustify(words []string, maxWidth int) []string {
	start := 0
	total := len(words)

	returnStrs := []string{}

	for {
		length := 0

		currentStart := start

		for {
			if start >= total {
				break
			}

			length += len(words[start])

			if length < maxWidth {
				start += 1
				length += 1
			} else if length == maxWidth {
				start += 1
			} else {
				break
			}
		}
		returnStrs = append(returnStrs, singleLinePadding(words[currentStart:start], maxWidth, start == total ))
		if start >= total {
			break
		}
	}
	return returnStrs
}

func main() {
	fullJustify([]string{ "This", "is", "an", "example", "of", "text", "justification.", "ad", "erf", "dsfdf"}, 16)
	fmt.Println(fullJustify([]string{ "This", "is", "an", "example", "of", "text", "justification.", }, 16))
}
