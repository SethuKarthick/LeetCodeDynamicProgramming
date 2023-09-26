func maxProfit(k int, prices []int) int {
    // buy := make([]int, k+1)
    // sell := make([]int, k+1)

    // for i:= range buy{
    //     buy[i] = math.MaxInt
    // }

    // for _, price := range prices {
    //     for i:=1; i<=k; i++{
    //         buy[i] = min(buy[i], price-sell[i-1])
    //         sell[i] = max(sell[i], price-buy[i])
    //     }
    // }
    // return sell[k]
    n := len(prices)
    if n == 0 {return 0}
    dp := make([]int, n)

    if k > n{
        B := []int{}
        for i:=1; i<n; i++{
            B[i-1] = prices[i] - prices[i-1] 
        }
        sum := 0
        for _, v := range B{
            if v > 0{
                sum += v
            }
        }
        return sum
    }

    for t :=0; t<k; t++{
        pos := -prices[0]
        profit := 0
        for i:=1; i<n; i++{
            pos = max(pos, dp[i]-prices[i])
            profit = max(profit, pos+prices[i])
            dp[i] = profit
        } 
    }
    return dp[len(dp)-1]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// func min(a, b int ) int {
//     if a < b{
//         return a 
//     }
//     return b
// }