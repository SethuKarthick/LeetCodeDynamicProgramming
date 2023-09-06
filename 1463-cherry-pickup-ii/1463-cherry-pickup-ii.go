func cherryPickup(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])


    memo := make([][][]int, 2)
    for i:= range memo{
        memo[i] = make([][]int, n)
        for j:= range memo[i]{
            memo[i][j] = make([]int, n)
            for k:= range memo[i][j]{
                memo[i][j][k] = -1
            }
        }
    }

    move := []int{-1, 0, 1}

    for row := m-1; row>= 0; row--{
        for col1:=0; col1<n; col1++{
            for col2:=0; col2<n; col2++{
                res:= grid[row][col1]
                if col1!= col2{
                    res+= grid[row][col2]
                }
                if row!= m-1{
                    max:= 0
                    for i:= range move{
                        for j:= range move{
                            preCol1 := col1+move[i]
                            preCol2 := col2+move[j]
                            if preCol1 < 0 || preCol1 >=n || preCol2 <0 || preCol2 >= n{
                                continue
                            }
                            max =  getMax(max, memo[(row+1)%2][preCol1][preCol2])
                        }
                    }
                    res += max
                }
                memo[row%2][col1][col2] = res
            }
        }
    }
    return memo[0][0][n-1]
}

func getMax(a, b int) int {
    if a > b{
        return a 
    }
    return b
}