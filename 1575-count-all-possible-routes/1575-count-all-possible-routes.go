func countRoutes(locations []int, start int, finish int, fuel int) int {
    lenLocations := len(locations)
    states := make([]int, lenLocations*(fuel+1))
    const mod = 1e9+7

    for i:= range states{
        states[i] = -1
    }

    toState := func(curPos, curFuel int) int {
        return curPos + curFuel * lenLocations
    }

    var dfs func(curPos, curFuel int) int
    dfs = func(curPos, curFuel int) int {
        if states[toState(curPos, curFuel)] != -1{
            return states[toState(curPos, curFuel)]
        }

        res := 0
        for nextPos := range locations{
            if nextPos != curPos {
                if abs(locations[curPos] - locations[nextPos]) <= curFuel{
                    res += dfs(nextPos, curFuel - abs(locations[curPos] - locations[nextPos]))
                }
            } 
        }
        if curPos == finish{
            res += 1
        }
        states[toState(curPos, curFuel)] = res % mod
        return res % mod
    }
    dfs(start, fuel)
    return states[toState(start, fuel)]
}

func abs(n int) int {
    if n > 0{
        return n 
    }
    return -n
}