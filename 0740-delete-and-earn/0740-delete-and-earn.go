func deleteAndEarn(nums []int) int {
    l :=  10002
    dp := make([]int, 10002)
    for _, v := range nums{
        dp[v] += v
    }

    a := dp[l-2]
    b := 0

    for i:=l-3; i>=0; i--{
        c := max(dp[i]+ b, a)
        b = a
        a = c
        // dp[i] = max(dp[i-1], max(dp[i-2], dp[i-3])+ dp[i])
    }
    // return dp[10001]
    return a

    
}

func max(a, b int) int{
    if a > b {
        return a
    }
    return b
}