func maxProfit(k int, prices []int) int {
    buy := make([]int, k+1)
    sell := make([]int, k+1)

    for i:= range buy{
        buy[i] = math.MaxInt
    }

    for _, price := range prices {
        for i:=1; i<=k; i++{
            buy[i] = min(buy[i], price-sell[i-1])
            sell[i] = max(sell[i], price-buy[i])
        }
    }
    return sell[k]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int ) int {
    if a < b{
        return a 
    }
    return b
}