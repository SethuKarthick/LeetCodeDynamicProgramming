func deleteAndEarn(nums []int) int {
    dp := make([]int, 10003)
    for _, v := range nums{
        dp[v] += v
    }
    for i:=3; i<=10001; i++{
        dp[i] = max(dp[i-1], max(dp[i-2], dp[i-3])+ dp[i])
    }
    return dp[10001]
}

func max(a, b int) int{
    if a > b {
        return a
    }
    return b
}