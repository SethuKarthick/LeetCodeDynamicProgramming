import "math"

func stoneGameIII(stoneValue []int) string {
    dp := make([]int, len(stoneValue))
    sum := make([]int, len(stoneValue)+1)
    
    for i:=0; i< len(stoneValue); i++{
        sum[i+1] = sum[i] + stoneValue[i]
        dp[i] = math.MinInt64
    }
    
    for i:= len(stoneValue)-1; i>=0; i--{
        for x:= 1; x<=3; x++{
            if i+x >= len(stoneValue){
                dp[i] = max(dp[i], sum[len(stoneValue)] - sum[i])
                break
            }else {
                dp[i] = max(dp[i], sum[len(stoneValue)]-sum[i]-dp[i+x])
            }
            
        }
    }
    if dp[0] * 2 > sum[len(stoneValue)]{
        return "Alice"
    }else if dp[0]*2 == sum[len(stoneValue)]{
        return "Tie"
    }else {
        return "Bob"
    }
}

func max(a, b int) int{
    if a > b{
        return a 
    }
    return b
}