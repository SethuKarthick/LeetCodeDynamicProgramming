func minPathCost(grid [][]int, moveCost [][]int) int {
    cost := make([]int, len(grid[0]))
    copy(cost, grid[len(grid)-1])
    for i:=len(grid)-2; i>= 0; i--{
        newCost := make([]int, len(grid[0]))
        copy(newCost, grid[i])
        for idx, nc := range newCost{
            minCost:= math.MaxInt64
            for order, mc := range moveCost[nc]{
                curCost := mc+cost[order]+nc
                if curCost < minCost{
                    minCost = curCost
                }
            }
            newCost[idx] = minCost
        }
        copy(cost, newCost)
    }
    return min(cost...)
}

func min(values ...int) int {
    minValue := math.MaxInt64
    for _, v := range values {
        if v < minValue{
            minValue = v
        }
    }
    return minValue
}