package main

import "fmt"


var (
	CheckStack *Stack
)

type Stack struct {
	Eles []*RuleEle
	top  int
	size int
}

func (stack *Stack) Enqueue(rule *RuleEle) {

	if stack.top >= stack.size {
		panic("not enough space for stack")
	}

	stack.Eles[stack.top] = rule
	stack.top += 1
}


func (stack *Stack) Clear() {
	stack.top = 0
}

func (stack *Stack) Top() *RuleEle {

	if stack.top == 0 {
		return nil
	}

	return stack.Eles[stack.top - 1]
}

func (stack *Stack) Dequeue() *RuleEle {

	if stack.top == 0 {
		panic("stack is empty")
	}

	stack.top -= 1
	return stack.Eles[stack.top]
}

type RuleEle struct {
	t string
	start    int
	end      int
	missing  int
}

func isScrambleByIdx(idxArray []int) bool {
	fmt.Println(idxArray)
	last := -1

	CheckStack.Clear()
	bitArray := make([]bool, len(idxArray))
	for idx, _ := range bitArray {
		bitArray[idx] = false
	}

	for idx, val := range idxArray {
		bitArray[val] = true
		if idx == 0 {
			last = val
			continue
		}

		for {
			top := CheckStack.Top()
			if top == nil {
				break
			}
			if val > top.start && val < top.end {
				top.missing -= 1
				if top.missing == 0 {
					CheckStack.Dequeue()
					continue
				}
			} else if (val < top.start || val > top.end) && top.missing > 0 {
				return false
			}
			break
		}


		var t string
		var start int
		var end int

		if val > last + 1 {
			t = "+"
			start = last + 1
			end = val
		} else if val < last - 1 {
			t = "-"
			start = val + 1
			end = last
		}

		if t != "" {
			missing := 0
			//fmt.Println(bitArray)
			for i :=start;i <end;i++ {
				if ! bitArray[i] {
					missing += 1
				}
			}
			rule := &RuleEle{
				t:t,
				start:start - 1,
				end: end,
				missing: missing,
			}
			CheckStack.Enqueue(rule)
			//fmt.Println(rule, idx, val, start, end, missing)
		}

		last = val
	}
	return true
}

type IterEle struct {
	char byte
	idxs []int
	cursor int
}


func enumberCombination(s2 string, idx int, mapping map[byte]map[int]int, idxArray []int) bool {
	if idx == len(s2) {
		return isScrambleByIdx(idxArray)
	}

	char := s2[idx]
	subMapping, _ := mapping[char]

	for key, value := range subMapping{
		if value == 1 {
			idxArray[idx] = key
			subMapping[key] = 0
			re := enumberCombination(s2, idx + 1, mapping, idxArray)
			if re {
				return true
			}
			subMapping[key] = 1
		}
	}
	return false
}

func isScramble(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	length := len(s1)
	CheckStack = &Stack{
		Eles: make([]*RuleEle, length),
		top: 0,
		size: length,
	}
	chaMapping := make(map[byte][]int)
	for idx, chr := range []byte(s1) {
		array, ok := chaMapping[chr]
		if ok {
			array = append(array, idx)
		} else {
			array = []int{idx}
		}
		chaMapping[chr] = array
	}

	idxMapping := make(map[byte]map[int]int)
	for _, char := range []byte(s2) {
		array, _ := chaMapping[char]
		if _, ok := idxMapping[char]; !ok {
			mapping := make(map[int]int)
			for _, value := range array {
				mapping[value] = 1
			}
			idxMapping[char] = mapping
		}
	}
	return enumberCombination(s2, 0, idxMapping, make([]int, len(s2)))
}



func main() {
	fmt.Println(isScramble("12345", "52413"))
	fmt.Println(isScramble("abcd", "cbda"))
	fmt.Println(isScramble("bdac", "abcd"))

	fmt.Println(isScramble("abcd", "acdb"))
}