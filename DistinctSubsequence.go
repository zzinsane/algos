package main

import "fmt"

type Ele struct {
	Idx     int

	Options []int
	Current int
}

var (

	byteMapping = make(map[byte][]int)
	cache = make(map[string]int)

)

func numDistinctRecursion(t string, s string, indexT, indexS int) int {
	key := fmt.Sprintf("%d_%d", indexT, indexS)
	if value, ok := cache[key]; ok {
		return value
	}

	if indexT >= len(t) - 1 {
		indexes := byteMapping[t[indexT]]
		for _, v := range indexes{
			if v >= indexS {
				return 1
			}
		}
		return 0
	}

	total := 0
	b := t[indexT + 1]
	indexes := byteMapping[b]
	for _, v := range indexes {
		if v > indexS {
			a:=numDistinctRecursion(t, s, indexT + 1, v)
			total += a
		}
	}

	cache[key] = total

	return total
}


func numDistinct(s string, t string) int {
		if len(s) < len(t) {
		return 0
		}

	if len(s) == 0 || len(t) == 0 {
		return 1
	}

	byteMapping = make(map[byte][]int)
	cache = make(map[string]int)

	for idx, b := range s {
		if array, ok := byteMapping[byte(b)]; ok {
			array = append(array, idx)
			byteMapping[byte(b)] = array
		} else {
			byteMapping[byte(b)] = []int{idx}
		}
	}

	total := 0
	a := t[0]
	indexes := byteMapping[a]
	for _, index := range indexes {
		a:=numDistinctRecursion(t, s, 0, index)
		total+= a
	}

	return total
}

//func numDistinct(s string, t string) int {
//
//	for idx, b := range s {
//		if array, ok := byteMapping[byte(b)]; ok {
//			array = append(array, idx)
//			byteMapping[byte(b)] = array
//		} else {
//			byteMapping[byte(b)] = []int{idx}
//		}
//	}
//	if len(t) == 1 {
//		return len(byteMapping[t[0]])
//	}
//
//	optionStack := make([]*Ele, len(t))
//	for idx, b := range t {
//		idxes , ok:= byteMapping[byte(b)]
//		if !ok {
//			return 0
//		}
//		optionStack[idx] = &Ele{
//			Idx:idx,
//			Options:idxes,
//			Current:0,
//		}
//	}
//
//	top := -1
//	length := len(t)
//	idx := 0
//	total := 0
//
//	for {
//
//		ele := optionStack[idx]
//
//		if ele.Current >= len(ele.Options) {
//			if idx == 0 {
//				return total
//			}
//
//			idx -= 1
//			top = 0
//			optionStack[idx].Current += 1
//			continue
//		}
//
//		start := ele.Current
//		for i:= ele.Current;i<len(ele.Options);i++ {
//			if ele.Options[i] > top {
//				break
//			}
//			start += 1
//		}
//
//		if start >= len(ele.Options){
//			idx-=1
//			top = 0
//			optionStack[idx].Current += 1
//			continue
//		}
//
//		ele.Current = start
//		top = ele.Options[ele.Current]
//
//		if idx == length - 1 {
//			total += len(ele.Options) - ele.Current
//
//			idx -= 1
//			top = 0
//			optionStack[idx].Current += 1
//			continue
//		}
//
//		idx += 1
//		optionStack[idx].Current = 0
//	}
//
//}

func main(){

	fmt.Println(numDistinct("", "a"))
	fmt.Println(numDistinct("", ""))
	fmt.Println(numDistinct("rabbbit", "rabbit"))
	fmt.Println(numDistinct("b", "b"))
	fmt.Println(numDistinct("aba", "ab"))
	fmt.Println(numDistinct("erete", "ee"))
	//fmt.Println(numDistinct("abab", "ab"))
	fmt.Println(numDistinct("adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc", "bcddceeeebecbc"))
}
