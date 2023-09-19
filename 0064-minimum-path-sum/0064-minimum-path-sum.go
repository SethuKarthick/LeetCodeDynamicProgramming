func minPathSum(grid [][]int) int {
    for i, v := range grid{
        for j:= range v{
            if i>0 && j> 0{
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            }else if i > 0 {
                grid[i][0] += grid[i-1][0]
            }else if j>0{
                grid[0][j] += grid[0][j-1]
            }
        }
    }
    return grid[len(grid)-1][len(grid[0])-1]
}

func min(a, b int) int {
    if a < b{
        return a 
    }
    return b
}