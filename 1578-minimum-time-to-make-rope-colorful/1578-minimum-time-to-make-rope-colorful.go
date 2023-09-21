func minCost(colors string, neededTime []int) int {
    totalTime := 0

    for i:= 1; i< len(colors); i++{
        if colors[i] == colors[i-1]{
            totalTime += min(neededTime[i], neededTime[i-1])
            if neededTime[i] < neededTime[i-1]{
                neededTime[i], neededTime[i-1] = neededTime[i-1], neededTime[i]
            }
        }
    }
    return totalTime
}

func min(a, b int ) int {
    if a < b {
        return a
    }
    return b
}