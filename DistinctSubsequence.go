package main

import "fmt"

type Ele struct {
	Idx     int

	Options []int
	Current int
}
//
//type Stack struct {
//	Eles []*Ele
//	top int
//	Size int
//}
//
//func (stack *Stack) Pop() {
//	if stack.top == 0{
//		return nil
//	}
//	stack.top -= 1
//	return stack.Eles[stack.top]
//}
//
//func (stack *Stack) Top(){
//	if stack.top == 0 {
//		return nil
//	}
//	return stack.Eles[stack.top]
//}
//
//func (stack *Stack) Push(ele *Ele){
//	stack.Eles[stack.top] = ele
//	stack.top += 1
//}

func numDistinct(s string, t string) int {

	byteMapping := make(map[byte][]int)
	for idx, b := range s {
		if array, ok := byteMapping[byte(b)]; ok {
			array = append(array, idx)
			byteMapping[byte(b)] = array
		} else {
			byteMapping[byte(b)] = []int{idx}
		}
	}

	//stack := &Stack{
	//	Eles:make([]*Ele, len(t)),
	//	top: 0,
	//	Size: len(t),
	//}
	optionStack := make([]*Ele, len(t))


	for idx, b := range t {
		idxes , ok:= byteMapping[byte(b)]
		if !ok {
			return 0
		}

		optionStack[idx] = &Ele{
			Idx:idx,
			Options:idxes,
			Current:0,
		}
	}

	top := -1
	//for idx, b := range t {
	length := len(t)
	idx := 0
	total := 0
	for {

		ele := optionStack[idx]

		if ele.Current >= len(ele.Options) {
			if idx == 0 {
				return total
			}

			idx -= 1
			optionStack[idx].Current += 1
			fmt.Println("idx:", idx)
			continue
		}

		start := ele.Current
		for i:= ele.Current;i<len(ele.Options);i++ {
			if ele.Options[i] > top {
				break
			}
			start += 1
		}

		if start >= len(ele.Options){
			idx-=1
			optionStack[idx].Current += 1
			continue
		}

		ele.Current = start
		top = ele.Options[ele.Current]

		if idx == length - 1 {
			total += len(ele.Options) - ele.Current
			for a:=0;a<=idx;a++ {
				fmt.Printf("%+v\n", optionStack[a])
			}

			fmt.Println("------")
			idx -= 1
			optionStack[idx].Current += 1
			continue
		}

		idx += 1
		optionStack[idx].Current = 0

	}

}

func main(){

	fmt.Println(numDistinct("rabbbit", "rabbit"))
}
