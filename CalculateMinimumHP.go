package main

import "fmt"
import "math"

type HP struct {
	MinHP int
	CurrentHP int
}

func calculateMinimumHP(dungeon [][]int) int {
	lengthX := len(dungeon[0])
	lengthY := len(dungeon)

	HP4Step := make([][][]*HP, lengthY)
	for i:=0;i<lengthY;i++ {
		HP4Step[i] = make([][]*HP, lengthX)
		//for k:=0;k<lengthX;k++ {
		//	HP4Step[i][k] = make([]*HP, 0)
		//}
	}

	initial := 1
	if dungeon[0][0] < 0 {
		initial = - dungeon[0][0] + 1
	}
	HP4Step[0][0] = []*HP {
		&HP{
			MinHP:initial,
			CurrentHP: dungeon[0][0],
		},
	}

	for i := 0;i<lengthX;i++ {
		for k:=0;k<lengthY;k++ {
			HPS := make([]*HP, 0)

			if i > 0 {
				for _, iHP := range HP4Step[i - 1][k] {
					current := iHP.CurrentHP + dungeon[i][k]

					minHP := 1
					if current < 0 {
						minHP = - current + 1
					}

					HPS = append(HPS, &HP{
						MinHP: int(math.Max(float64(minHP), float64(iHP.MinHP))),
						CurrentHP: current,
					})
				}
			}

			if k > 0 {
				for _, iHP := range HP4Step[i][k - 1] {
					current := iHP.CurrentHP + dungeon[i][k]


					minHP := 1
					if current < 0 {
						minHP = - current + 1
					}

					HPS = append(HPS, &HP{
						MinHP: int(math.Max(float64(minHP), float64(iHP.MinHP))),
						CurrentHP: current,
					})
				}
			}
			if ! (i ==0 && k == 0) {
				HP4Step[i][k] = HPS
			}

			//	preCost = int(math.Max(float64(dungeon[i-1][k]), float64(dungeon[i][k-1])))
			//} else if i > 0 {
			//	preCost = dungeon[i-1][k]
			//} else if k > 0 {
			//	preCost = dungeon[i][k-1]
			//}
			//dungeon[i][k] = preCost + dungeon[i][k]
		}
	}
	fmt.Println(dungeon)

	for i:=0;i<lengthX;i++ {

		for k:=0;k<lengthY;k++ {
			for _, cHP := range HP4Step[i][k] {
				fmt.Printf("%d_%d:  %d %d, \n", i, k, cHP.MinHP, cHP.CurrentHP)
			}
		}
	}
	fmt.Println(HP4Step)
	return 0
}
func main() {
	fmt.Println(calculateMinimumHP(
		[][]int{
			[]int{-2,-3,3},
			[]int{-5,-10,1},
			[]int{10,30,-5},
		},
	))
}
